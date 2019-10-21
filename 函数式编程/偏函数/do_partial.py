# -*- coding: utf-8 -*-

import  functools
print(int('12345'))
print(int('12345',base=8))
print(int('12345',8))
print(int('12345',16))

#定义一个int2()的函数，默认把base=2传进去
def int2(x, base=2):
    return int(x,base)

#测试
#按二进制转换
print(int2('1000000'))
print(int2('1010101'))
#这样不会报错
print('result:',int2('1010101',10))
print('result:',int2('1010101',base=10))

int2New = functools.partial(int,base=2)
print(int2New('1000000'))
print(int2New('1010101'))
# 注意到上面的新的int2函数，仅仅是把base参数重新设定默认值为2，但也可以在函数调用时传入其他值：
print(int2New('1000000', base=10))
#这样会报错
#print(int2New('1000000', 10))

kw = {'base': 2}
print(int('10010', **kw))
print(int2New('10010'))
print(int2('10010'))

max2 = functools.partial(max,10)
print('max:',max2(5,6,7))

args = (10,5,6,7)
print('max:',max(*args))

