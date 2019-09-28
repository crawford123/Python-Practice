for x in [1, 2, 3, 4, 5]:
    print(x)
    
print('===================')
#实际上完全等价于
it = iter([1, 2, 3, 4, 5])
# 循环
while True:
    try:
        #获得下一个值
        x = next(it)
        print(x)
    except StopIteration:
        # 遇到StopIteration，就退出循环
        break