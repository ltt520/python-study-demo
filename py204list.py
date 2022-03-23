# -*- coding: utf-8 -*-

#1
print('\n#1')
zlst=['hello','PyQt5','.','com']
vlst=['Top','Quant','.','vip']
print('zlst,',zlst)
print('vlst,',vlst)

#test—mystudy
zlst.append("ltt")
print('zlst', zlst)
t = ['1',  '2']
zlst.extend(t)
print('zlst', zlst)
#2
print('\n#2')
s2=zlst[1:];print('s2,',s2)
s3=zlst[1:3];print('s3,',s3)
s4=vlst[:3];print('s4,',s4)

#3
print('\n#3')
print('s2+s3,',s2+s3)
# 加号是列表连接运算符，乘号是重复运算
print('s3*2,',s3*2)

