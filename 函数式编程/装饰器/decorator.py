# -*- coding: utf-8 -*-

def now():{
    print("2015-03-25")
}

print("now:",now)
f = now
print("f",f)
print("f():",f())
print("now.__name__:",now.__name__)
print("f.__name__:",f.__name__)
