from collections import namedtuple
from typing import NamedTuple

Person = namedtuple('Person', 'name job birthday')
jim = Person('jim', 'salesman', birthday='1/8/78')


class Person(NamedTuple):
    name: str
    job: str
    birthday: str


dwight = Person('dwight', job='assistant to the regional manager', birthday='20/1/70')

# this only works in python 3.7 onwards
from dataclasses import dataclass


@dataclass
class Person:
    name: str
    job: str
    birthday: str = None


micheal = Person('micheal', job='regional manager')
