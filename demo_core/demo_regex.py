import re

pattern = re.compile("([A-Z][a-z]+)'s (cat|dog|parrot|fish)[:, ]\s*([A-Z]?[a-z]+)")

story = \
    """
    Jim's dog, spot went to the park. There he saw Annie's cat: Snickers and Bob's dog alfonzo.
    They talked about Mr.Tailor's fish, toto. 
    """

for pet in pattern.finditer(story):
    owner, kind, name = pet.groups()
    print(f'{owner} has a {kind} named {name}')
