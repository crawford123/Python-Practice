# -*- coding: utf-8 -*-
#匿名函数
def f(x):
    return x * x
print(list(map(lambda x : x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9])))
print(list(map(f,[1, 2, 3, 4, 5, 6, 7, 8, 9])))

#匿名函数也是一个函数对象,可以把匿名函数赋值给一个变量，再利用变量来调用该函数：
f = lambda x: x * x
print("f:",f)
print("f(5):",f(5))

#可以把匿名函数作为返回值返回
def build(x,y):
    return lambda:x * x + y * y
print("build:",build(1,3))
t = build(2,3)
print("t:",t) #返回值与build一样，都是同一个匿名函数
print("t()",t())
