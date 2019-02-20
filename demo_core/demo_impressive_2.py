from typing import Dict, Mapping, Tuple, Union, List, Any, Callable, FrozenSet
from abc import abstractmethod, ABC

from numbers import Real
from collections import Counter
import re
import itertools as it


class FalseWrapper:
    def __init__(self, v):
        self.v = v

    def __bool__(self):
        return False

    def __call__(self):
        return self.v


def _combine_maps(func: Callable[..., int], *maps: Mapping[Any, int], default=0) -> Counter:
    keys = it.chain(*(m.keys() for m in maps))
    ret = Counter()
    for k in keys:
        if k in ret:
            continue
        args = (m.get(k, default) for m in maps)
        v = func(*args)
        if v != default:
            ret[k] = v
    return ret


_float_args_pattern = re.compile(r'^(?P<float>[-+]?[0-9]*(\.[0-9]*)?([eE][-+]?[0-9]+)?)\s+(?P<meas>.*)')


def split_float_args(arg):
    match = _float_args_pattern.fullmatch(arg)
    if match and match.group('float'):
        return float(match.group('float')), match.group('meas')
    return 1, arg


class Unit(ABC):
    @abstractmethod
    def __getitem__(self, item: str) -> float:
        pass

    @abstractmethod
    def __contains__(self, item) -> bool:
        pass

    @abstractmethod
    def __primitives__(self) -> Counter:
        pass

    @abstractmethod
    def native_unit(self) -> str:
        pass

    @abstractmethod
    def root(self, r) -> 'Unit':
        pass

    def __mul__(self, other: 'Unit'):
        primitives = _combine_maps(lambda x, y: x + y, self.__primitives__(), other.__primitives__())
        return CompositeUnit(primitives)

    def __truediv__(self, other: 'Unit'):
        primitives = _combine_maps(lambda x, y: x - y, self.__primitives__(), other.__primitives__())
        return CompositeUnit(primitives)

    def __pow__(self, power: Union[int, Real]):
        if power not in [0, 1, -1] and (1 / power) % 1 == 0:
            return self.root(int(1 / power))
        primitives = _combine_maps(lambda x: x * power, self.__primitives__())
        return CompositeUnit(primitives)

    def __call__(self, measurement: Union[str, float], amount: Union[str, float] = 1) -> 'Measurement':
        if isinstance(measurement, Real) and isinstance(amount, str):
            amount, measurement = measurement, amount

        amount *= self[measurement]
        return Measurement(amount, self)

    def __getattr__(self, item):
        return self(item, 1)

    def __invert__(self):
        return ScalarUnit() / self

    def __rtruediv__(self, other: int):
        if other != 1:
            return NotImplemented
        return ~self


class ScalarUnit(Unit, int):
    singleton = None

    def __new__(cls):
        if not cls.singleton:
            cls.singleton = int.__new__(cls, 1)
        return cls.singleton

    def __getitem__(self, item):
        raise KeyError(item)

    def __contains__(self, item):
        return False

    def __primitives__(self):
        return Counter()

    def native_unit(self):
        return None

    def __repr__(self):
        return f'{type(self).__name__}()'

    def root(self, r):
        return self


class PrimitiveUnit(Unit):
    def __init__(self, name: str, **units: Union[float, str, Tuple[float, str]]):
        self.name = name
        self._dict = units

    def __setitem__(self, key: str, value: Union[float, str, Tuple[float, str]]):
        self._dict[key] = value

    def __getitem__(self, item):
        if isinstance(item, Measurement):
            if item.unit != self:
                raise ValueError(f'cannot accept measurement of unit {item}')
            return item.amount
        a, item = split_float_args(item)
        if a != 1:
            return a * self[item]
        ret = self._dict[item]
        if isinstance(ret, str):
            return self[ret]

        try:
            amount, unit = ret
        except (ValueError, TypeError):
            pass
        else:
            return amount * self[unit]

        return ret

    def __contains__(self, item):
        return item in self._dict

    def __primitives__(self):
        return Counter({self: 1})

    def __str__(self):
        return self.name

    def __hash__(self):
        return hash(self.name)

    def native_unit(self):
        return next(iter(self._dict))

    def root(self, r):
        if r == 1:
            return self
        raise ValueError('cannot get root of primitive unit')


class CompositeUnit(Unit):
    composite_measurement_pattern = re.compile(
        r'(?P<pos>(([a-zA-Z]+((\^|(\*\*)|())[1-9][0-9]*)?)(\s*\*?\s*[a-zA-Z]+((^|(\*\*)|())[1-9][0-9]*)?)*)|1)'
        r'(\s*\/\s*(?P<neg>([a-zA-Z]+((\^|(\*\*)|())[1-9][0-9]*)?)(\s*\*?\s*[a-zA-Z]+((^|(\*\*)|())[1-9][0-9]*)?)*))?'
    )
    measurement_pattern = re.compile(r'((?P<name>[a-zA-Z]+)((\^|(\*\*)|())(?P<num>[1-9][0-9]*))?)')
    cache: Dict[FrozenSet[Tuple[PrimitiveUnit, int]], 'CompositeUnit'] = {}

    @staticmethod
    def _fix_counter(c: Mapping[PrimitiveUnit, int]) -> FrozenSet[Tuple[PrimitiveUnit, int]]:
        return frozenset(c.items())

    def __new__(cls, parts: Counter):
        parts_key = cls._fix_counter(parts)
        if not parts_key:
            return ScalarUnit()
        if len(parts_key) == 1 and next(iter(parts_key))[1] == 1:
            return next(iter(parts_key))[0]

        try:
            return cls.cache[parts_key]
        except KeyError:
            pass

        ret = super().__new__(cls)
        cls.cache[parts_key] = ret
        return ret

    def __init__(self, parts: Counter):
        self._parts = parts
        self._aliases: Dict[str, Tuple[float, str]] = {}
        self._name = None

    def __primitives__(self):
        return self._parts

    def __contains__(self, item) -> Union[FalseWrapper, List[Tuple[PrimitiveUnit, int, str]]]:
        if item in self._aliases:
            f, a = self._aliases[item]
            return a in self
        match = self.composite_measurement_pattern.fullmatch(item)
        if not match:
            return FalseWrapper(ValueError(f'could not parse string {item!r}'))
        pos, neg = match.group('pos'), match.group('neg')
        assigned = []
        left = dict(self._parts)
        try:
            self._assign_measurements(pos, 1, assigned, left)
            self._assign_measurements(neg, -1, assigned, left)
        except KeyError as e:
            return FalseWrapper(e)

        for p, n in left.items():
            if n > 0:
                return FalseWrapper(KeyError(f'unit {p} unassigned'))

        return assigned

    @classmethod
    def _assign_measurements(cls, part: str, factor: int, assigned: List[Tuple[PrimitiveUnit, int, str]],
                             left: Dict[PrimitiveUnit, int]):
        if part is None or part == '1':
            return
        matches = cls.measurement_pattern.finditer(part)
        for m in matches:
            num = m.group('num')
            num = int(num) if num else 1
            num *= factor
            name = m.group('name')
            for p in (k for (k, n) in left.items() if n >= num):
                if name in p:
                    assigned.append((p, num, name))
                    left[p] -= num
                    assert left[p] >= 0
                    break
            else:
                raise KeyError(name)

    def __getitem__(self, item):
        if isinstance(item, Measurement):
            if item.unit != self:
                raise ValueError(f'cannot accept measurement of unit {item}')
            return item.amount
        a, i = split_float_args(item)
        if a != 1:
            return a * self[i]

        if item in self._aliases:
            a = self._aliases[item]
            if isinstance(a, str):
                f = 1
            else:
                f, a = a
            return f * self[a]
        assigned = self.__contains__(item)

        if not assigned:
            raise assigned()
        factor = 1
        for k, n, m in assigned:
            factor *= (k[m] ** n)

        return factor

    def __setitem__(self, key, value):
        if key == slice(None):
            self._name = value
            return
        self._aliases[key] = value

    def __str__(self):
        if self._name is not None:
            return self._name
        pos = []
        neg = []
        for m, n in self._parts.items():
            if n > 0:
                amount = '' if n == 1 else f'**{n}'
                pos.append(f'{m}{amount}')
            else:
                amount = '' if n == -1 else f'**{-n}'
                neg.append(f'{m}{amount}')
        if not pos:
            pos = ['1']
        return ' * '.join(pos) + '/' + ' * '.join(neg)

    def native_unit(self, compact=False):
        pos = []
        neg = []
        for m, n in self._parts.items():
            if n > 0:
                amount = '' if n == 1 else f'**{n}'
                pos.append(f'{m.native_unit()}{amount}')
            else:
                amount = '' if n == -1 else f'**{-n}'
                neg.append(f'{m.native_unit()}{amount}')
        if not pos:
            pos = ['1']
        separator = '*' if compact else ' * '
        pos = separator.join(pos)
        if not neg:
            return pos
        div = '/' if compact else ' / '
        neg = separator.join(neg)
        return ''.join((pos, div, neg))

    def root(self, r: int):
        if not all(n % r == 0 for n in self._parts.values()):
            raise ValueError(f'cannot get the {r} root of {self}')
        primitives = _combine_maps(lambda x: x / r, self.__primitives__())
        return CompositeUnit(primitives)


class Measurement:
    format_pattern = re.compile(
        r'((?P<inner_format>(.?[<>=^])?[-+ ]?#?0?[0-9]*[,_]?(\.[0-9]*)?[eEfFgGn%]?):)?'
        r'(?P<convert>[^:]*)(:(?P<display>.*))?')

    def __new__(cls, amount, unit):
        if unit is ScalarUnit():
            return amount
        return super().__new__(cls)

    def __init__(self, amount: float, unit: Unit):
        self.amount = amount
        self.unit = unit

    def __mul__(self, other: Union['Measurement', Real]):
        if isinstance(other, Real):
            return type(self)(self.amount * other, self.unit)
        if isinstance(other, Measurement):
            unit = self.unit * other.unit
            amount = self.amount * other.amount
            return type(self)(amount, unit)
        raise TypeError

    def __truediv__(self, other: Union['Measurement', Real]):
        if isinstance(other, Real):
            return type(self)(self.amount / other, self.unit)
        if isinstance(other, Measurement):
            unit = self.unit / other.unit
            amount = self.amount / other.amount
            return type(self)(amount, unit)
        raise TypeError

    def __rmul__(self, other: Real):
        return self * other

    def __rtruediv__(self, other: Real):
        return type(self)(other / self.amount, ~self.unit)

    def __pow__(self, power: int):
        return type(self)(self.amount ** power, self.unit ** power)

    def __add__(self, other: 'Measurement'):
        assert self.unit == other.unit
        return type(self)(self.amount + other.amount, self.unit)

    def __sub__(self, other: 'Measurement'):
        assert self.unit == other.unit
        return type(self)(self.amount - other.amount, self.unit)

    def __eq__(self, other: Union['Measurement', int]):
        if other == 0:
            return self.amount.__eq__(other)
        return self.unit == other.unit and self.amount == other.amount

    def __round__(self, measurement: Union[str, 'Measurement']):
        amount = self.unit[measurement]
        amount = amount * round(self.amount / amount)
        return type(self)(amount, self.unit)

    def __hash__(self):
        return hash((self.unit, self.amount))

    def __lt__(self, other: Union['Measurement', int]):
        if other == 0:
            return self.amount.__lt__(other)
        if self.unit != other.unit:
            return NotImplemented
        return self.amount.__lt__(other.amount)

    def __le__(self, other: Union['Measurement', int]):
        if other == 0:
            return self.amount.__le__(other)
        if self.unit != other.unit:
            return NotImplemented
        return self.amount.__le__(other.amount)

    def __gt__(self, other: Union['Measurement', int]):
        if other == 0:
            return self.amount.__gt__(other)
        if self.unit != other.unit:
            return NotImplemented
        return self.amount.__gt__(other.amount)

    def __ge__(self, other: Union['Measurement', int]):
        if other == 0:
            return self.amount.__ge__(other)
        if self.unit != other.unit:
            return NotImplemented
        return self.amount.__ge__(other.amount)

    def __getitem__(self, item):
        return self.amount / self.unit[item]

    def __repr__(self):
        return f'{self.amount} {self.unit.native_unit()}'

    def __format__(self, format_spec):
        match = self.format_pattern.fullmatch(format_spec)
        if not match:
            raise ValueError('could not parse format string ' + format_spec)
        float_format, convert, display = match.group('inner_format', 'convert', 'display')
        if not convert:
            convert = self.unit.native_unit()
        if not display:
            display = convert
        if not float_format:
            float_format = ''
        amount = self[convert]
        return f'{amount:{float_format}} {display}'

    def __neg__(self):
        return type(self)(-self.amount, self.unit)

    def root(self, r: int):
        return type(self)(self.amount ** (1 / r), self.unit.root(r))


Distance = PrimitiveUnit('distance', meter=1, kilometer=1000, km='kilometer', mile=1609.344)
Time = PrimitiveUnit('time', second=1, minute=60, hour=3600, day=(24, 'hour'))

Speed = Distance / Time

Acceleration = Speed / Time

assert Acceleration is Distance / Time ** 2

g = Acceleration('meter/second2', 9.8)

assert round(Speed(0.98, 'meter/second') / Time(0.1, 'second'), '0.1 meter/second**2') == g

sq_km = (Distance ** 2)('kilometer**2')
km = Distance.km
assert km ** 2 == sq_km

Frequency = 1 / Time
Frequency['hz'] = '1/second'
assert (Frequency['hz'] / Frequency['1/minute']) == 60

c = 299_792 * Distance.km / Time.second
assert g * Time.day < c

Mass = PrimitiveUnit('mass', kilogram=1, gram=0.001, ton=1000, kg='kilogram', lb=0.4536)

Force = Mass * Acceleration

Energy = Mass * Distance ** 2 / Time ** 2

assert Energy == Force * Distance

loki_mass = Mass(525, 'lb')

loki_momentum = loki_mass * g * 30 * Time.minute

print(f'in Thor: Ragnarok, loki hit the ground with {loki_momentum:,.0f:kilogram*meter/second:kg*m/s} of momentum')

# let's include terminal velocity

terminal_velocity = ((2 * loki_mass * g) / (
            (1.23 * Mass.kg / Distance.meter ** 3) * 1.008 * (Distance.meter ** 2))) ** .5

time_to_reach_tv = terminal_velocity / g
if 30 * Time.minute > time_to_reach_tv:
    loki_momentum = loki_mass * terminal_velocity

print(
    f'in Thor: Ragnarok, loki actually hit the ground with '
    f'{loki_momentum:,.0f:kilogram*meter/second:kg*m/s} of momentum')

Speed['mps'] = 'meter/second'
speed_of_sound = Speed('340 mps')
print(f'light is {c/speed_of_sound:,.0f} times faster than sound')
