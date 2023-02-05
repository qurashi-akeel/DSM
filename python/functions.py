# var args
def test(*args):
    return args  # args is tuple


print(test(1, 2, [0, 5, "j"]))


# keyword args
def test2(**kwargs):
    return kwargs  # kwargs is dictionary


print((test2(a=1, b="b")))

# Both


def both(*args, **kwargs):
    return args, kwargs


print(both(1, "b", a=5))  # ((1, 'b'), {'a': 5})
