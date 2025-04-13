# -*- coding: utf-8 -*-
"""
File Name: 检查变量类型.py

@author: lengf
@date: 2025-04-13
@email: lengfo@163.com
@version: 1.0.0
"""


# 检查变量类型
# type()函数可以用来检查变量的类型
# 语法：type(变量名)
# 返回值：变量的类型
# 示例：

a = 100
b = 1000000000000000000
c = 12.345
d = 1 + 5j
e = 'A'
f = 'hello, world'
g = True
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
print(type(g))

tuple1 = (1, 2, 3)
list1 = [4, 5, 6]
set1 = {7, 8, 9}
dict1 = {'name': 'lengf', 'age': 25}
print(type(tuple1))
print(type(list1))
print(type(set1))
print(type(dict1))

class Person:
    pass

p = Person()
print(type(p))     # 输出class Person 

print(type(None))   # 输出NoneType类型
print(range(10))
print(type(range(10)))    # 输出range类型
print(type(lambda x: x+1))    # 输出函数类型
print(type(abs))    # builtin_function_or_method 类型 意思是内置函数或方法
print(type(print))   # 同上 ，是内置函数或方法
print(type(type))     # 输出class type  意思是类类型
print(type(int))    #   输出class int    意思是类int
print(Person)   # 输出Person类     
print(type(Person))   # 输出Person类