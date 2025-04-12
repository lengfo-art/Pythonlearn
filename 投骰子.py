"""
掷骰子决定做什么事情
使用match语句来判断掷出的点数
比if-elif-else语句更简洁

Version: 0.2
Author: 林风
Date: 2025-04-10


Author: 骆昊
Date: 2018-02-28
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