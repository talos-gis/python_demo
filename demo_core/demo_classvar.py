class A:
    a = 12  # these variables belong to the class
    x = 'x'

    def __init__(self, a):
        self.a = a


v = A(9)
assert v.a == 9
assert A.a == 12
assert v.x == A.x == 'x'
assert A.__init__
