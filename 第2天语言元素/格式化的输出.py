# -*- coding: utf-8 -*-
"""
File Name: 格式化的输出.py

@author: lengf
@date: 2025-04-13
@email: lengfo@163.com
@version: 1.0.0
"""


# 格式化输出
# 输出使用的是print()函数，但如果需要格式化输出，可以使用字符串格式化方法。
# 字符串格式化方法是通过在字符串中插入变量，并用大括号{}包含变量名，来实现格式化输出的。
# 格式化输出的语法如下：
# 字符串 % 变量名
# 其中，% 是一个特殊字符，表示格式化输出的开始。
# 变量名可以是整数、浮点数、字符串、元组、列表等。
# 格式化输出的结果是一个字符串。

# 以下是一些示例：


a = int(input('a = '))
b = int(input('b = '))
print('%d + %d = %d' % (a, b, a + b))
print('%d - %d = %d' % (a, b, a - b))
print('%d * %d = %d' % (a, b, a * b))
print('%d / %d = %f' % (a, b, a / b))
print('%d // %d = %d' % (a, b, a // b))
print('%d %% %d = %d' % (a, b, a % b))
print('%d ** %d = %d' % (a, b, a ** b))



# 现在推荐使用f-string格式化输出，它是Python 3.6版本引入的新语法。
# 比前面的字符串格式化方法更简洁、直观。
# f-string格式化输出的语法如下：
# f'{表达式}'
# 其中，表达式可以是任意有效的Python表达式，可以包括变量、运算符、函数调用等。
# f-string格式化输出的结果是一个字符串。

# 以下是一些示例：

a = int(input('a = '))
b = int(input('b = '))
print(f'{a} + {b} = {a + b}')
print(f'{a} - {b} = {a - b}')
print(f'{a} * {b} = {a * b}')
print(f'{a} / {b} = {a / b:.2f}')    # 保留两位小数
print(f'{a} // {b} = {a // b}')
print(f'{a} %% {b} = {a % b}')
print(f'{a} ** {b} = {a ** b}')