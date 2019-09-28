L1 = ['Hello', 'World', 18, 'Apple', None]
#第一种写法
L2 = [s.lower() for s in L1 if isinstance(s, str) == True]
#第二钟写法
L3 = [s.lower() for s in L1 if isinstance(s, str)]

#第三种写法
L4 = []
for i in L1:
    #use 'is' is ok , use '==' is also ok
    if isinstance(i, str) == True:
    #if isinstance(i, str) is True:
        L4.append(i.lower())


#测试：
print(L2)
if L2 == ['hello', 'world', 'apple']:
    print("测试通过！")
else:
    print("测试失败！")