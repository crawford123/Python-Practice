# -*- coding: utf-8 -*-
import functools

def now():{
    print("2015-03-25")
}

print("now:",now)
f = now
#print("f:",f)
print("f():",f())
print("now.__name__:",now.__name__)
print("f.__name__:",f.__name__)

def log(func):
    def wrapper(*args, **kw):
        print(' call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

@log
def now1():
    print('2015-3-25')

print("now1:", now1)
print("now1():",now1())
now2 = log(now1)
print('now2:',now2)

#自定义log的文本
def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator
#3层嵌套的decorator用法如下
@log('execute')
def now3():
    print('2015-3-25')

print("now3 test:", now3)
now3 = log('execute')(now3)
print("now3 log:", now3)
print("now3()", now3())
print("now3'name:",now3.__name__)

#因为返回的那个wrapper()函数名字就是'wrapper'，所以，需要把原始函数的__name__等属性复制到wrapper()函数中，否则，有些依赖函数签名的代码执行就会出错。
def log1(func):
    #相当于wrapper.__name__ = func.__name__
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print(' call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

#或者针对带参数的decorator：
def log2(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args,**kw)
        return wrapper
    return decorator

@log1
def now4():
    print("2019-10-21")

@log2('execute')
def now5():
    print("2019-10-21")

print("now4:",now4)
print("now4():",now4())
print("now4:",now4.__name__)
print("now5:",now5)
print("now5():",now5())
print("now5:",now5.__name__)