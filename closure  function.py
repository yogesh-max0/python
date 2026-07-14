def outer(msg):
    def inner():
        return f"{msg}"
    return inner

hi = outer('this is closure function')
print(hi())


'''
---------------------------------------------------------------------------
'''


def outer():
    x = 10
    def inner():
        return x
    return inner

f = outer()
print(f())