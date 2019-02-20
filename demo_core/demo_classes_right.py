class Date:
    def __init__(self, day, month):
        self.day = day
        self.month = month

    def __str__(self):
        month_names = {
            1: 'jan', 2: 'feb', 3: 'mar',
            4: 'apr', 5: 'may', 6: 'jun',
            7: 'jul', 8: 'aug', 9: 'sep',
            10: 'oct', 11: 'nov', 12: 'dec'
        }
        month = month_names[self.month]
        return f'{month} {self.day}'

    def is_winter(self):
        return self.month in (12, 1, 2)

    def day_of_week(self, year):
        if not 2017 <= year <= 2019:
            raise ValueError('no leap years')  # spoilers
        ret = 0  # jan 1st 2017 was a sunday
        year_offset = 365 % 7
        ret += year_offset * (year - 2017)
        month_offsets = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31,
                         8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
        for i in range(1, self.month):
            ret += month_offsets[i]
        ret += self.day - 1  # there are 2 problems in programming...
        day_names = {0: 'sunday', 1: 'monday', 2: 'tuesday', 3: 'wednesday',
                     4: 'thursday', 5: 'friday', 6: 'saturday'}
        ret %= 7
        return day_names[ret]


pagan_days = {
    "Valentine's": Date(14, 2),
    "St. Patrick's": Date(17, 3),
    'Easter': Date(1, 4),
    'Halloween': Date(31, 10),
    'Christmas': Date(25, 12)
}
for name, when in pagan_days.items():
    print(f'{name} 2018 will be a {when.day_of_week(2018)}')
