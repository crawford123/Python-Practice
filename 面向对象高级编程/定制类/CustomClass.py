# -*- coding: utf-8 -*-

#__iter__
class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1 # 初始化两个计数器a，b

    def __iter__(self):
        return self # 实例本身就是迭代对象，故返回自己

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b # 计算下一个值
        if self.a > 100000: # 退出循环的条件
            raise StopIteration()
        return self.a # 返回下一个值

for n in Fib():
    print(n)

# __getitem__
class Fib(object):
    def __getitem__(self, n):
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
f = Fib()
print(f[0])
print(f[4])

print(list(range(100))[5:10])
#这样会报错，原因是__getitem__()传入的参数可能是一个int，也可能是一个切片对象slice
#print(f[:10])
class Fib(object):
        def __getitem__(self, n):
            if isinstance(n, int):
                a, b = 1, 1
                for x in range(n):
                    a, b = b, a + b
                return a
            if isinstance(n, slice):#n是切片
                start = n.start
                stop = n.stop
                if start is None:
                    start = 0
                a, b = 1, 1
                L = []
                for x in range(stop):
                    if x >= start:
                        L.append(a)
                    a, b = b, a + b
                return L
#测试
f = Fib()
print(f[0:5])
print(f[:10])

#__getattr__
#注意，只有在没有找到属性的情况下，才调用__getattr__，已有的属性，比如name，不会在__getattr__中查找。
class Student(object):
    def __init__(self):
        self.name = 'Michael'
    #当调用不存在的属性时，比如score，Python解释器会试图调用__getattr__(self, 'score')来尝试获得属性
    def __getattr__(self, attr):
        if attr == 'score':
            return 99
        #返回函数也是可以的
        if attr == 'age':
            return lambda: 25
        raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)
 #测试
s = Student()
print(s.name)
#调用不存在的score属性会报错
print(s.score)
print(s.age())
# 会raise出AttributeError
#print(s.abc)

class Chain(object):
    def __init__(self, path=''):
        self._path = path
    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))
    def __str__(self):
        return self._path
    __repr__ = __str__

print(Chain().status.user.timeline.list)

#__call__
class Student(object):
    #实例化Student类时一定要带name参数
    def __init__(self, name):
        self.name = name
    def __call__(self):
        print('My name is %s.' % self.name)

#测试
s = Student('Michael')
s1 = Student("")
# self参数不要传入
print(s())
print(s1())
print(s1)
#通过callable()函数，我们就可以判断一个对象是否是“可调用”对象。
#比如函数和我们上面定义的带有__call__()的类实例
print(callable(Student("hhh")))
print(callable(s1))
print(callable([1,2,3]))
print(callable(None))
print(callable('str'))
print(callable(min(1,-2))) #为false
print(min(1,-2))
#print(abs(1,2))