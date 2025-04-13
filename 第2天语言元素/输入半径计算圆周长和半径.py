# -*- coding: utf-8 -*-
"""
File name: 输入半径计算圆周长和半径.py

@author: lengf
@date: 2025-04-13
@email: lengfo@163.com
@version: 1.0.0
"""



import math     # 导入math模块


print('请输入半径计算圆周长和面积')

#增加捕获异常处理
try:
    radius = float(input('请输入圆的半径: '))
# 计算圆周长和面积
# 圆周长 = 2 * pi * r
# 面积 = pi * r^2
    permimeter = 2*math.pi*radius
    area = math.pi*radius*radius
    print(f'周长: {permimeter:.2f}')
    print(f'面积: {area:.2f}')

except ValueError:
    print('输入的不是数字，需要输入数字！')