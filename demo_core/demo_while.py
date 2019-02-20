x = 'i am groot'
while x:  # strings are considered True while they are not empty
    print(x)
    x = x[:-1]  # remove the last letter (we'll explain this later)
