# -*- coding: utf-8 -*-
"""
File Name: 变量理解保存指向的数据地址.py

@author: lengf
@date: 2025-04-13
@email: lengfo@163.com
@version: 1.0.0
"""


x = 10     
y = x
print(id(x))    # 打印x的内存地址   10的内存地址
print(id(y))    # 打印y的内存地址    10的内存地址
print(x is y)  # 判断x和y是否指向同一内存地址 True
print(id(10))   # 打印10的内存地址  10的内存地址

x = 20
print(id(x))    # 打印x的内存地址   20的内存地址
print(id(y))    # 打印y的内存地址     10的内存地址
print(x is y)  # 判断x和y是否指向同一内存地址   False
print(id(20))   # 打印20的内存地址  20的内存地址


str1 = ["hello", "world"]
str2 = str1
print(id(str1))   # 打印str1的内存地址  
print(id(str2))   # 打印str2的内存地址 
print(str1 is str2)  # 判断str1和str2是否指向同一内存地址 True
print(str1 is ["hello", "world"])  # 判断str1和["hello", "world"]是否指向同一内存地址 False
              # print语句中参数的列表是创建了一个新的列表，与str1指向的列表不是同一个内存地址


print(str1 == ["hello", "world"])  # 判断str1和["hello", "world"]是否内容相同 True

''' is 和 == 区别总结
# 运算符	作用	示例	结果
# is	比较内存地址（是否同一个对象）	x is y	True 仅当 x 和 y 是同一个对象
# ==	比较值（内容是否相同）	x == y	True 只要 x 和 y 的值相同
'''