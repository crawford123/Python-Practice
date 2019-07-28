#循环
names = ['Michael','Bob','Tracy']
for name in names:
    print(name)
    
#计算1-10的整数之和，可以用一个sum变量做累加：
sum = 0
for x in [1,2,3,4,5,6,7,8,9,10]:
    sum = sum+x
print(sum)    

# 打印出range(0, 5)，可以生成一个整数序列(从0开始小于5的整数)
#range函数可以生成一个整数序列
print(range(5))
#把range(3)表示成list的形式，不能这样打印出来
#print(list(range(5))

sum = 0 
for x in range(101):
    sum = sum + x
print(sum)
 
# while循环  计算100以内所有奇数之和
sum = 0
n = 99
while n>0: 
    sum = sum+n
    n = n-2
print(sum)

#练习题
L = ['Bart','Lisa','Adam']
#第一种写法
print('第一种写法')
for name in L:
    print('hello,%s!' %name)
#第二种写法
print('第二种写法')
#range(3)可以，list(range(3))也可以
for i in range(3):
    print('hello,%s!' %L[i])

#第三种写法
print('第三种写法')
n = 0
while n<3:
    print('hello,%s!' %L[n])
    n = n+1

    
    
#break 作用是提前结束循环。
n = 1
while n <= 100:
    if n > 10: #当n = 11时，条件满足，执行break语句
        break # break语句会结束当前循环
    print(n)
    n = n+1
print('END')
#continue  跳过当前的这次循环，直接开始下一次循环
n = 0
while n<10:
    n = n+1
    if n%2 ==0:# 如果n是偶数，执行continue语句
        continue # continue语句会直接继续下一轮循环，后续的print()语句不会执行
    print(n)
print('END')
#试写一个死循环程序
#第一种写法
#while(True):
#   print('I love you')
#第二种写法
#while 1:
 #   print('死了')

 
 



    
    
