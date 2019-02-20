# lines starting with "#" are comments will be ignored

string = 'hello world'  # comments can also appear after a line

for character in string:  # lines ending with ":" start a new block
    print(character)  # all indented lines are considered inside the block
# to exit the block, just remove the indent
# take care to either use 4 spaces or 1 tab as indent, both cause messy code
# pycharm automatically replaces your tabs with 4 spaces

if string.startswith('hello'): string = string + '!'  # don't actually do this

print(string)

import time  # importing a non-standard function
time.sleep(0.5)  # wait for half a second

print(string/3)  # python will try to run this line, but fail
