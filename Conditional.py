#age = input('please input your age: ')
age=78
if age >= 18:
    print('your age is',age)
    print('adult')
else:
    print('your age is',age)
    print('teenager')
    
#age = input('please input your age: ')
#print('your age is',age)

#完全可以用elif做更细致的判断：
age = 2
if age >= 18:
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('kid')

#只要x是非零数值、非空字符串、非空list等，就判断为True，否则为False。
if 8:
    print('True')
else:
    print('False')
    
#Python提供了int()函数
s = input('birth:')
birth = int(s)
if birth<2000:
    print('00前')
else:
    print('00后')