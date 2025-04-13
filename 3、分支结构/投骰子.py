# -*- coding: utf-8 -*-
"""
File Name:    投骰子.py

@author: lengf
@date: 2025-04-13
@email: lengfo@163.com
@version: 1.0.0
使用match语句实现投骰子游戏，根据随机生成的数字，输出对应的动作。


"""



from random import randint

face = randint(1, 6)  # 随机生成1到6的整数
print(f'你掷出了{face}点')
# if face == 1:
#     result = '唱首歌'
# elif face == 2:
#     result = '跳个舞'
# elif face == 3:
#     result = '学狗叫'
# elif face == 4:
#     result = '做俯卧撑'
# elif face == 5:
#     result = '念绕口令'
# else:
#     result = '讲冷笑话'
# print(result)
 #     改进版：使用match语句
match face:
    case 1:
        print('唱首歌')
    case 2:
        print('跳个舞')
    case 3:
        print('学狗叫')
    case 4:
        print('做俯卧撑')
    case 5:
        print('念绕口令')
    case _:
        print('讲冷笑话')