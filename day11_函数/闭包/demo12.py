funcs = []


def register(func):
    funcs.append(func)
    return func


@register
def a():
    return 3


@register
def b():
    return 5


result = [func() for func in funcs]
print(result)
