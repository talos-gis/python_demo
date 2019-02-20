month_names = {
            1: 'jan', 2: 'feb', 3: 'mar',
            4: 'apr', 5: 'may', 6: 'jun',
            7: 'jul', 8: 'aug', 9: 'sep',
            10: 'oct', 11: 'nov', 13: 'dec',
        }

assert all(i in month_names for i in range(1, 13))
assert all(isinstance(month_names[i], str) for i in range(1, 13)), 'a value in the dictionary is not a string'
