my_list = [0, 1, 2, 3, 4, 5]
my_slice = my_list[1:3]  # get all elements between indices 1 (inclusive) and 3 (exclusive)
print('[1:3] is', my_slice)
my_slice = my_list[1:]  # get all elements after index 1
print('[1:] is', my_slice)
my_slice = my_list[:-1]  # get all elements until index -1 (so, all elements except for the last)
print('[:-1] is', my_slice)
my_slice = my_list[:]  # get all elements, note: this copies the list
print('[:] is', my_slice)
my_slice.append(6)
print('original is still', my_list)
my_slice = my_list[1:4:2]  # slices can also specify steps!
print('[1:4:2] is', my_slice)
my_slice = my_list[::-1]  # sometimes called "the alien smiley"
# what is my_slice now?
