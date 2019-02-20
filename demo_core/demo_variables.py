x = 3
# the name x is now linked with the value 3
print('x is', x)

# the following line will cause an error if run
print(y)
# since y is not defined yet

y = 'hi'

print(y)

x = 4  # x is now changed to be 4
x = x + 1  # x is now increased by 1
x += 1  # this is the same as the above line
print(x)

y *= x
print(y)

# this won't work
y = y+x
# why? Python is dynamically typed, but not weakly typed!
