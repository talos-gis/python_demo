from datetime import date


class Person:
    def __init__(self, first_name: str, last_name: str, title: str = ''):
        self.first_name = first_name.capitalize()
        self.last_name = last_name.capitalize()
        self.title = title

    @property
    def full_name(self):
        return f'{self.title}{self.first_name} {self.last_name}'

    def uses_matlab(self):
        return self.title in ['Dr.', 'Prof.']


class Worker(Person):
    def __init__(self, first_name: str, last_name: str, birth_date: date, title: str = ''):
        super().__init__(first_name, last_name, title)
        self.birth_date = birth_date

    def uses_matlab(self):
        return self.birth_date.year < 1960 \
               or super().uses_matlab()


tom = Worker('tom', 'smith', birth_date=date(1987, 2, 3), title='Prof.')
print(tom.uses_matlab())
