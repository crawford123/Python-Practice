# -*- coding: utf-8 -*-
n1 = 255
n2 = 1000
print(hex(255),hex(1000))

#defining function
def my_abs(x):
    if x>= 0:
        return x
    else:
        return -x
        
#defining function 添加了参数检查，进行错误和异常处理
def my_abs1(x):
    if not isinstance(x,(int,float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x
#抛出错误
#print(my_abs1('2'))
print(my_abs1(True))
print(my_abs1(False))
print(my_abs1(-2))
print(my_abs1(-2.5))
        

#call function
print(my_abs(-99))
print(my_abs(0))

#定义空函数
#如果想定义一个什么事也不做的空函数，可以用pass语句：
def nop():
    pass
# pass还可以用在其他语句里,缺少了pass，代码运行就会有语法错误。
age = 19
if age >= 18:
    pass  
else:
    print(age)
    
#返回多个值
import math

def move(x, y, step, angle=0):
    nx = x + step*math.cos(angle)
    ny = y - step*math.sin(angle)
    return nx,ny

x,y = move(100,100,60,math.pi / 6)
print(x,y)

r = move(100,100,60,math.pi / 6)
print(r)

#定义一元二次方程的求根函数
def quadratic(a,b,c):
    #确认是否有实根
    z = b**2-4*a*c
    if z < 0:
        print('无实根')
    else:
        x1=(-b+math.sqrt(z))/2*a
        x2=(-b-math.sqrt(z))/2*a
        return x1,x2
    
#测试代码
#返回无实根，打印出None
print(quadratic(1,1,1))
print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))

if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
else:
    print('测试成功')
    
if quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')
    
#递归函数
def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)
  
#针对尾递归做优化，解决递归调用栈溢出的方法 
#即使把上面的fact(n)函数改成尾递归方式，也会导致栈溢出。
def facts(n):
    return fact_iter(n, 1)

#return fact_iter(num - 1, num * product)仅返回递归函数本身，num - 1和num * product在函数调用前就会被计算，不影响函数调用
def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)

#经过测试，还是会导致栈溢出
#print(facts(1000))

#函数的参数
#位置参数
def power(x):
    return x * x
    
def powers(x, n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
       

#power(x)修改为power(x, n)，用来计算x的n次方
#设定第二个参数n的默认值设定为2：
def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
    

#相当于调用power(5, 2)：
#而对于n > 2的其他情况，就必须明确地传入n，比如power(5, 3)。
print(power(5))
print(power(5,2))
print(power(5,3))

#更多例子
def enroll(name,gender):
    print('name:',name)
    print('gender:',gender)
    
#设置默认参数
def enroll(name,gender,age=6,city='Beijing'):
    print('name',name)
    print('gender:',gender)
    print('age:',age)
    print('city:',city)
    
#只有与默认参数不符的学生才需要提供额外的信息：
#可以按顺序提供默认参数
enroll('Bob', 'M', 7)
#也可以不按顺序提供默认参数
enroll('Adam', 'M', city='Tianjin')

#默认参数的坑
#定义一个函数，传入一个list，添加一个END再返回：
def add_end(L=[]):
    L.append('END')
    return L
#测试代码，函数每次都“记住了”上次添加了'END'后的list。
add_end()   
#优化后的函数
#我们在编写程序时，如果可以设计一个不变对象，那就尽量设计成不变对象。
def add_ends(L=None):
    if L is None:
        L = []
    L.append('END')
    return L
    
#可变参数
#普通的函数
def calc(numbers):
    sum=0
    for n in numbers:
        sum=sum+n*n
    return sum
#需要如下调用：
#calc(1, 2, 3)
#calc(1, 3, 5, 7)
#改变为可变参数,重写了
def calc(*numbers):
    sum=0
    for n in numbers:
        sum=sum+n*n
    return sum

#如果已经有一个list或者tuple，可以采取如下调用
#第一种方法
#nums = [1, 2, 3]
#calc(nums[0], nums[1], nums[2])
#第二钟方法 list或tuple的元素变成可变参数传进去：
#calc(*nums)

#关键字参数
#这些关键字参数在函数内部自动组装为一个dict
def person(name,age,**kw):
    print('name:',name,'age:',age,'other:',kw)

def persons(name,age,**kw):
    if 'city' in kw:
       print(kw['city']) 
       kw['city']='Beijing'
    # 有city参数
    if 'job' in kw:
       print(kw['job']) 
       kw['job']='Nurse'
     # 有job参数
    print('name:',name,'age:',age,'other:',kw)
    
#使用pass语法
def person_pass(name,age,**kw):
    if 'city' in kw:
        pass
    if 'job' in kw:
        pass
    print('name:',name,'age:',age,'other:',kw)
    
#命名关键字参数
#命名关键字参数必须传入参数名，这和位置参数不同。如果没有传入参数名，调用将报错
def person_name(name,age,*,city,job):
    print(name,age,city,job)
    
def person_name1(name,age,*args,city,job):
    print(name,age,args,city,job)
    
def person_name2(name,age,*,city='Beijing',job):
    print(name,age,city,job)

def person_name3(name, age, city, job):
    # 缺少 *，city和job被视为位置参数
    pass

#参数组合
#参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
#比如定义一个函数，包含上述若干种参数：
def f1(a,b,c=0,*args,**kw):
    print('a=',a,'b=',b,'c=',c,'agrs=',args,'kw=',kw)

#默认参数可以如下的调用格式    
#f1(1, 2, c=3)
    
def f2(a,b,c=0,*,d,**kw):
    print('a=',a,'b=',b,'c=',c,'d=',d,'kw=',kw)

def f3(a,b,c=0,*,d=3,**kw):
    print('a=',a,'b=',b,'c=',c,'d=',d,'kw=',kw)
    
#设计一个接收一个或多个数并计算乘积的函数,
#第一种写法,3
#最后测试成功
def product(*x):
    s=1
   #当x为()时，直接跳过循环返回
    for i in x:
        s = s * i
    return s
    
#第二钟方法
#最后测试失败
def product(a,*x):
    s=a
   #当x为()时，直接跳过循环返回
    for i in x:
        s=s*i
    return s
#测试代码
print('product(5) =', product(5))
print('product(5, 6) =', product(5, 6))
print('product(5, 6, 7) =', product(5, 6, 7))
print('product(5, 6, 7, 9) =', product(5, 6, 7, 9))
if product(5) != 5:
    print('测试失败!')
elif product(5, 6) != 30:
    print('测试失败!')
elif product(5, 6, 7) != 210:
    print('测试失败!')
elif product(5, 6, 7, 9) != 1890:
    print('测试失败!')
else:
    try:
        product()
        print('product() =', product())
        print('测试成功!')
    except TypeError:
        print('测试失败!')


    
    

    

   


    
   

