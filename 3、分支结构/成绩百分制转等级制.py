# -*- coding: utf-8 -*-
"""
File Name: 成绩百分制转等级制.py

@author: lengf
@date: 2025-04-13
@email: lengfo@163.com
@version: 1.0.0

代码功能：
1. 输入成绩，判断等级并输出
2. 转成match case语句 ，但可读性更好。

"""


# score = float(input('请输入成绩: '))
# if score >= 90:
#     grade = 'A'
# elif score >= 80:
#     grade = 'B'
# elif score >= 70:
#     grade = 'C'
# elif score >= 60:
#     grade = 'D'
# else:
#     grade = 'E'
# print('对应的等级是:', grade)

# # 把上面代码转成match case语句

# 加一个try except 防止输入非数字.  给了一次机会，并提醒重新输入
# 可以加一个while循环，让用户一直输入直到输入正确为止。

score = input('请输入成绩: ')
try:
    score = float(score)
except ValueError:
    print('输入非数字，请重新输入')
    score = input('请输入成绩: ')
    score = float(score)
grade = ''    # 定义一个空字符串，用来接收等级
match score:   # 定义match case语句
    case score if score >= 90:   
        grade = 'A'
    case score if score >= 80:
        grade = 'B' 
    case score if score >= 70:
        grade = 'C'
    case score if score >= 60:
        grade = 'D'
    case _:
        grade = 'E'
print('对应的等级是:', grade)