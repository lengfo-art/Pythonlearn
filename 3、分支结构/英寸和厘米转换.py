# -*- coding: utf-8 -*-
"""
File Name: 英寸和厘米转换.py

@author: lengf
@date: 2025-04-13
@email: lengfo@163.com
@version: 1.0.0
"""

# 定义常量
# 使用函数进行转换
# 输入输出格式化

INCH_TO_CM = 2.54

def convert_length(value, unit):
    if unit in ('in', '英寸'):
        return value * INCH_TO_CM
    elif unit in ('cm','厘米'):
        return value / INCH_TO_CM
    else:
        return '请输入有效的单位(in/英寸或cm/厘米)'
    
value = float(input('请输入长度：'))      # 注意没加try-except, 输入错误不能转换成数字的话会直接报错
unit = input('请输入单位：').lower().strip()  # 转换为小写并去除空格

result = convert_length(value, unit)
if isinstance(result, float):    # 判断是否为浮点数
    # print('%f%s = %f%s' % (value, unit, result, '厘米' if unit in ('in', '英寸') else '英寸'))
    print(f'{value:.2f}{unit} = {result:.2f}{"厘米" if unit in ("in", "英寸") else "英寸"}')   # 输出格式化，使用了f-string，在{}中使用了表达式，判断用户输入的单位，对应输出的转换单位。
else:
    print(result)    # 输出错误信息  