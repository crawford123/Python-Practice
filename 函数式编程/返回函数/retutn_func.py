# -*- coding: utf-8 -*-
# 函数作为返回值

def calc_sum(*args):
    ax = 0
    for n in args:
        ax = ax + n
    return ax


def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax

    return sum

print(range(1,4))
print(list(range(1, 4)))
print("calc_sum:",calc_sum(*range(1,4)))
print("lazy_sum1:",lazy_sum(*range(1,4)))
print("lazy_sum2:",lazy_sum(1,3,5,7,9))
f = lazy_sum(1,3,5,7,9)
print(f)
print(f())

# f1()和f2()的调用结果互不影响。
f1 = lazy_sum(1,3,5,7,9)
f2 = lazy_sum(1,3,5,7,9)
print("f1:",f1)
print("f2:",f2)
print(f1 == f2)

#闭包
def count():
    fs = []
    for i in range(1,4):
        def f():
            return i * i
        fs.append(f)
    return fs
f1,f2,f3 = count()
print("f1():",f1())
print("f2():",f2())
print("f3():",f3())
# 如果一定要引用循环变量怎么办？方法是再创建一个函数，用该函数的参数绑定循环变量当前的值
# 缺点是代码较长，可利用lambda函数缩短代码。
#返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量。
def count1():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1,4):
        print(i,f(i))
        fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
    return fs

f1,f2,f3 = count1()
print("f1():",f1())
print("f2():",f2())
print("f3():",f3())

