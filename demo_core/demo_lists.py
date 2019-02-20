list1 = []  # initialize as empty list
if list1:  # container types are true only if they have at least one element
    print('this will not be printed')

list2 = [1, 'one', 1.0]
print('list1 is', list1)
print('list2 is', list2)
print("list2's first element is", list2[0])  # indices in Python (like everywhere) are 0-based
print("list2's last element is", list2[-1])  # negative indices count from the end
list1.append('a new element')
print('list1 is', list1)
print('list1 has', len(list1), 'elements')

list1 = list2
print('list1 is', list1)
print('list2 is', list2)
# BEWARE! all non-primitive type in python is a reference type!
list2[1] = 'two'
print('list1 is now', list1)
print('list2 is now', list2)
