# -*- coding: utf-8 -*-
"""
File Name

@author: lengf
@date: 2025-04-13
@email: lengfo@163.com
@version: 1.0.0

功能描述：

实现华氏度转摄氏度和摄氏度转华氏度的转换。
程序流程：

1. 接受用户输入，提示输入F则执行华氏度转摄氏度的转换，如是C则执行摄氏度转华氏度的转换，如是Q则退出程序。
2. 输入华氏度或摄氏度，并进行转换。
3. 输出转换后的结果。
4. 循环执行步骤1。

"""

while True:
    choice = input('请输入F（华氏度转摄氏度）、或C（摄氏度转华氏度）或Q（退出程序）：')
    choice = choice.upper()                 # 转换为大写字母
    if choice == 'F':
        f = float(input('请输入华氏度：'))
        c = (f - 32) / 1.8
        print(f'{f}华氏度 = {c:.1f}摄氏度')
    elif choice == 'C':
        c = float(input('请输入摄氏度：'))
        f = c * 1.8 + 32
        print(f'{c}摄氏度 = {f:.1f} 华氏度')
    elif choice == 'Q':
        print('退出程序！')
        break
    else:
        print('输入错误，请重新输入！')



# 把上面代码转换成match-case语句

# while True:
#     choice = input('请输入F（华氏度转摄氏度）、或C（摄氏度转华氏度）或Q（退出程序）：')
#     choice = choice.upper()
#     match choice:
#         case 'F':
#             f = float(input('请输入华氏度：'))
#             c = (f - 32) / 1.8
#             print(f'{f}华氏度 = {c:.1f}摄氏度')
#         case 'C':
#             c = float(input('请输入摄氏度：'))
#             f = c * 1.8 + 32
#             print(f'{c}摄氏度 = {f:.1f} 华氏度')
#         case 'Q':
#             print('退出程序！')
#             break
#         case _:
#             print('输入错误，请重新输入！')
