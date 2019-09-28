# -*- coding: utf-8 -*-
# map/reduce
from functools import reduce

#map
def f(x):
    return x * x
r = map(f,[1,2,3,4,5,6,7,8,9])
print("r:",r)
print("list(r):",list(r))

#for循环
L = []
for n in [1,2,3,4,5,6,7,8,9]:
    L.append(f(n))
print("L:",L)

#reduce
#str转换为int的函数 两种方式
#第一种方式 lambda函数
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}


def char2num(s):
    return DIGITS[s]


def str2int(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))


def test():
    return "test"


print("test1:",str2int('13579'))
# print(str2int([1,3,5,7,9]))
print(test())


# 第二种方式 整理成一个str2int1的函数
def str2int1(s):
    def fn(x, y):
        return x * 10 + y

    def char2num1(s):
        return DIGITS[s]
    return reduce(fn, map(char2num1, s))


print("result2:",str2int1('13579'))
