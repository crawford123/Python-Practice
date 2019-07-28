#-*-coding:utf-8 -*-
#构造一个1, 3, 5, 7, ..., 99的列表，可以通过循环实现：
L = []
n=1
while n <= 99:
    L.append(n)
    n=n+2
print(L)
    
#定义一个trim()函数，去除字符串首尾的空格
#使用递归的方法 第一种方法
def trim(s):
    if len(s) == 0:
        return s
    if ' ' in s[0]:
        return trim(s[1:])
    elif ' ' in s[-1]:
        return trim(s[:-1])
    else:
        return s
#第二种方法
def trims(s):    
    if s == '':
        return s
    while s[:1]==' ':
        s = s[1:]
    while s[-1:] == ' ':
        s = s[:-2]
    return s

 # 测试:
if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')
    
    
if trims('hello  ') != 'hello':
    print('测试失败!')
elif trims('  hello') != 'hello':
    print('测试失败!')
elif trims('  hello  ') != 'hello':
    print('测试失败!')
elif trims('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trims('') != '':
    print('测试失败!')
elif trims('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')
    
#请使用迭代查找一个list中最小和最大值，并返回一个tuple
def findMinAndMax(L):
    if len(L)==0:
        return (None,None) 
    min = L[0]
    max = L[0]
    for i in L:
        if i<min:
            min=i
        elif i>max:
            max=i
    return (min,max)
 

# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')
