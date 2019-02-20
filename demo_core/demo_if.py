x = input()  # get a line from the user
if len(x) < 5:
    print('too short!')
    exit()

if x.startswith('hello'):
    if x.endswith('world') or x.endswith('world!'):
        # strings can be done either with a single or double quote
        print("sad truth: the world doesn't say hello back")
    elif x.endswith('python'):
        print('hiss')
    else:
        print('hi there!')
elif x == 'make me a sandwich':
    print('no')
elif x == 'sudo make me a sandwich':
    print('error: module "sand" not found')
elif 'matlab' in x:
    print("'end' statements are dumb")
else:
    print("I don't understand")
