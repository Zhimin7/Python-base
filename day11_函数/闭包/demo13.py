class Registry(object):
    def __init__(self):
        self.funcs = []

    def register(self, func):
        self.funcs.append(func)

    def return_all(self):
        return [func() for func in self.funcs]


r1 = Registry()
r2 = Registry()


@r1.register
def a():
    return 3


@r2.register
def b():
    return 5

