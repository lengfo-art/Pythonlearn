# -*- coding: utf-8 -*-
"""
File Name: 分段结构求值.py

@author: lengf
@date: 2025-04-13
@email: lengfo@163.com
@version: 1.0.0
"""




# 注意：分段函数的求值需要考虑边界条件，即函数在分段点处的取值
x = float(input('x = '))
if x > 1:
    y = 3 * x - 5
elif x >= -1:
    y = x + 2
else:
    y = 5 * x + 3
print('f(%.2f) = %.2f' % (x, y))


print(f'f({x:.2f}) = {y:.2f}')    # 使用f-string格式化输出，保留两位小数，并用括号包裹变量，避免出现语法错误，提高代码可读性，推荐使用，
     # 注意：f-string格式化输出只能用于python3.6及以上版本
     # 引号内的f  是输出的字符串，在这表示数学函数。
