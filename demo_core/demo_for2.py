for number in range(1, 21):
    # range's bounds are inclusive on the min and exclusive on the max
    if number % 7 != 0 and '7' not in str(number):
        print(number)
    else:
        print('boom')
