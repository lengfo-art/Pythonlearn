"""
输入半径计算圆的周长和面积
公式：周长 = 2 * pi * r，面积 = pi * r * r
增加功能：输入圆面积计算半径, 来验证计算公式是否正确
公式：r = sqrt(area / pi)

Version: 0.3

Version: 0.2
作者：林风
Date: 2025-04-10

"""

import math   # 导入math模块,在使用一些数学函数时会用到


radius = float(input('请输入圆的半径: '))
perimeter = 2 * math.pi * radius
area = math.pi * radius * radius

print('圆的半径为：', radius)
print(f'周长为：{perimeter:.2f}')
print(f'面积为：{area:.2f}')

# 增加功能：输入圆面积计算半径

area = float(input('请输入圆的面积: '))
radius = math.sqrt(area / math.pi)

print(f'圆的半径为：{radius:.2f}')
print(f'周长为：{2 * math.pi * radius:.2f}')