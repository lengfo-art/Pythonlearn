"""
检查变量的类型
数据类型有：整数、浮点数、复数、字符串、布尔值、列表、元组、字典、集合、范围、字节串、切片、迭代器、生成器等。

使用type()函数可以检查变量的类型。

Version: 0.1
Author: 林风
Date: 2025-04-10
"""

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

# 其他数据类型  
h = [1, 2, 3]
i = (1, 2, 3)
j = {'name': 'Alice', 'age': 25}
k = set([1, 2, 3])
l = frozenset([1, 2, 3])
m = {'name': 'Bob', 'age': 30}
n = b'hello, world'
o = range(10)
p = (1, 2, 3, ['a','b'])    
print(type(h))
print(type(i))
print(type(j))
print(type(k))
print(type(l))
print(type(o))
print(type(p[2:])) # 切片操作返回一个新的元组，因此类型仍然是元组
print(type(p[3])) # 列表类型 元组中索引为3的元素
print(type(m))
print(type(n))

