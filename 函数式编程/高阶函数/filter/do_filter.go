# -*- coding: utf-8 -*-

#在一个list中，删掉偶数，只保留奇数
def is_odd(n):
	return n % 2 ==1
	
test = list(filter(is_odd,[1,2,3,4,5,6,9,10,15]))
print("list:",test)

#把一个序列中的空字符串删掉，可以这么写：
def not_empty(s):
    return s and s.strip()
    
test1 = list(filter(not_empty, ['A', '', 'B', None, 'C', '    ']))
#filter()函数返回的是一个Iterator，也就是一个惰性序列，
print("filter:",filter(not_empty, ['A', '', 'B', None, 'C', '    ']))
print("test1,", test1)

#注意这是一个生成器，并且是一个无限序列。
def _odd_iter():
    n = 1
    while True:
        n = n+2
        yield n

#然后定义一个筛选函数：
def _not_divisible(n):
    return lambda x: x % n > 0

#定义一个生成器，不断返回下一个素数：
def primes():
    yield 2
    it = _odd_iter() #初始序列
    print('it:', it)
    while True:
        n = next(it) #返回序列的第一个数
        yield n
        it = filter(_not_divisible(n), it)

#打印1000以内的素数:
for n in primes():
    if n < 1000:
        print(n)
    else:
        break
        

        
 
        
   