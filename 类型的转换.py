"""
类型转换

Version: 0.1
Author: 骆昊
Date: 2018-02-27
"""
# 类型转换:
# 1. 整数和浮点数之间的转换
# 2. 字符串和数字之间的转换
# 3. 布尔值和字符串之间的转换
# 4. 字符串和布尔值之间的转换
# 5. 其他类型之间的转换
# 数据类型转换注意点：
# 1. 转换前后的数据类型必须兼容，否则会报错。
     #例如，不能把字符串转换成布尔值，除非字符串表示的布尔值。
     # 不能把字符串转换成整数，除非字符串表示的整数。
# 2. 转换过程中可能会丢失精度。
# 3. 转换过程中可能会导致数据溢出。
# 4. 转换过程中可能会导致数据精度损失。
# 5. 转换过程中可能会导致数据精度丢失。


a = 100
b = str(a)
c = 12.345
d = str(c)
e = '123'
f = int(e)
g = '123.456'
h = float(g)
i = False
j = str(i)
k = 'hello'
m = bool(k)


print(a)
print(type(a))
print(b)
print(type(b))
print(c)
print(type(c))
print(d)
print(type(d))
print(e)
print(type(e))
print(f)
print(type(f))
print(g)
print(type(g))
print(h)
print(type(h))
print(i)
print(type(i))
print(j)
print(type(j))
print(k)
print(type(k))
print(m)
print(type(m))
