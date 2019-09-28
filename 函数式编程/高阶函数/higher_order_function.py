# -*- coding: utf-8 -*-
def add(x, y ,f):
    return f(x) + f(y)

test = add(-5, 6, abs)
print(add(-5, 6, abs))
print("add:",test)