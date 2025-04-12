"""
输入年份 如果是闰年输出True 否则输出False
加入判断是否输入0退出程序。

Version: 0.1
Author: 林风
Date: 2025-04-10
"""

# year = int(input('请输入年份: '))
# # 如果代码太长写成一行不便于阅读 可以使用\或()折行
# is_leap = (year % 4 == 0 and year % 100 != 0 or
#            year % 400 == 0)
# print(is_leap)


# 定义一个匿名函数 作用是判断闰年，返回True或False
IS_LEAP = lambda year: (year % 4 == 0 and year % 100 != 0 or year % 400 == 0) 

while True:
    year = int(input('请输入年份:'))
    print('如果要退出请输入0')
    if year == 0:
        break
    print(IS_LEAP(year))
    
    
    
    