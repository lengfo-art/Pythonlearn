"""
英制单位英寸和公制单位厘米互换
转换公式：1英寸 = 2.54厘米
使用常量表示单位换算关系，并使用函数封装转换逻辑。
标准化处理用户输入，转成小写并去除空格。

Version: 0.2
Author: 林风
Date: 2025-04-10

Author: 骆昊
Date: 2018-02-28
"""

# value = float(input('请输入长度: '))
# unit = input('请输入单位: ')
# if unit == 'in' or unit == '英寸':
#     print('%f英寸 = %f厘米' % (value, value * 2.54))
# elif unit == 'cm' or unit == '厘米':
#     print('%f厘米 = %f英寸' % (value, value / 2.54))
# else:
#     print('请输入有效的单位')

INCH_TO_CM = 2.54

def convert_length(value, unit):
    if unit in ('in', '英寸'):
        return value * INCH_TO_CM
    elif unit in ('cm','厘米'):
        return value / INCH_TO_CM
    else:
        return '请输入有效的单位(in/英寸或cm/厘米)'
    
value = float(input('请输入长度：'))
unit = input('请输入单位：').lower().strip()  # 转换为小写并去除空格

result = convert_length(value, unit)
if isinstance(result, float):
    # print('%f%s = %f%s' % (value, unit, result, '厘米' if unit in ('in', '英寸') else '英寸'))
    print(f'{value:.2f}{unit} = {result:.2f}{"厘米" if unit in ("in", "英寸") else "英寸"}')
else:
    print(result)