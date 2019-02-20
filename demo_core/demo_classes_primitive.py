class Date:
    pass  # do nothing (for now)


christmas = Date()
# you can now fill it with whatever you want
christmas.day = 25
christmas.month = 12
print(christmas)


# huh, okay let's do this
def date_to_str(date):
    month_names = {
        1: 'jan', 2: 'feb', 3: 'mar',
        4: 'apr', 5: 'may', 6: 'jun',
        7: 'jul', 8: 'aug', 9: 'sep',
        10: 'oct', 11: 'nov', 12: 'dec'
    }
    # why a dict and not a list? sometimes abstractions are useful
    month = month_names[date.month]
    return f'{month} {date.day}'


print(date_to_str(christmas))


# while we're at it
def initialize_date(date, day, month):
    date.day = day
    date.month = month


halloween = Date()
initialize_date(halloween, 31, 10)
print(date_to_str(halloween))
