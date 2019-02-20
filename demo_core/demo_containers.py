# tuples
tup = 1, 2, 3
print(tup[1:])  # (2, 3)
tuptup = 1, (2, 3), 4
# unpacking
one, (two, three), four = tuptup
print(one, two, three, four)
# dicts
my_dict = {'jan': 1, 'feb': 2, 'mar': 3, 'smarch': 3.5}
print('feb' in my_dict)
print(my_dict['feb'])
# we won't go into everything dicts, sets, and lists can do.
# Type help(<type>) to see everything, for example
help(set)
