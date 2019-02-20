origin = range(10)  # 1,2,3,4,5,6,7,8,9
no_threes = filter(lambda x: x % 3 != 0, origin)  # 1,2,4,5,7,8
squares = map(lambda x: x**2, no_threes)  # 1,4,16,25,49,64
# squares is not a list!
print(squares)
# let's turn it into one
squares = list(squares)
print(squares)
# now let's do it in one line!
print(list(map(lambda x: x**2, filter(lambda x: x % 3 != 0, range(10)))))
# this is confusing, I wish we could just do
print([x**2 for x in range(10) if x % 3 != 0])
