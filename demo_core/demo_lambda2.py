my_list = [9, 15, 2, 6, 764, -1]
my_sorted_list = sorted(my_list, key=lambda x: x % 3)  # sort the list by modulo 3
print(my_sorted_list)
my_sorted_list = sorted(my_list, key=lambda x: (x % 3, x))  # sort first by mod 3, then by the element itself
print(my_sorted_list)
