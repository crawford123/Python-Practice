#!/usr/bin/env python3
# -*- coding: utf-8 -*-
print('中文测试正常')

print('%2d-%02d' %(3,1))
print('%.2f' %3.1415926)

s1 = 72
s2 = 85
r =  (s2-s1)/s1*100
print('His grade is improved by %.1f%%.'%r)
a = input('小明去年成绩为：')
b = input('小明今年成绩为：')
c = ((int(b)-int(a))/int(a))*100
print('小明成绩提高了%.1f%%'%c)