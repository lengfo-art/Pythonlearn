# -*- coding: utf-8 -*-
"""
File Name: 判断是否闰年.py

@author: lengf
@date: 2025-04-13
@email: lengfo@163.com
@version: 1.0.0

"""

# 程度功能：
# 提示用户输入年份
# 提示判断方法
# 处理异常输入
# 如是年份则判断是否闰年
# 如不是年份则提示输入正确的年份
# 输出判断结果
# 再次提示用户输入年份
# 直到输入Q退出程序

while True:
    try:
        year = input("请输入年份（输入Q退出程序）：")
        if year.upper() == "Q":
            break
    
        year = int(year)

        print("判断方法：")
        print("1. 若年份是4的倍数但不是100的倍数，则为闰年。")
        print("2. 若年份是400的倍数，则为闰年。")
        print("3. 其余年份均为平年。")
        if year < 1 or year > 9999:
            raise ValueError("年份必须大于0且小于9999")
        if year % 4 == 0 and (year % 100!= 0 or year % 400 == 0):
            print(year, "是闰年")
        else:
            print(year, "不是闰年")
    except ValueError as e:
        print("输入错误，请输入正确的年份：", e)

