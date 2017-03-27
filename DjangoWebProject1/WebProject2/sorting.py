a=10

def func(b):
    global a
    #a=30
    return a+b

print(func(10))


def f():
    a=30
    def g():
        nonlocal a
        a=40
    g()
    return a

print(f())