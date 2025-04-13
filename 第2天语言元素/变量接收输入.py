# -*- coding: utf-8 -*-
"""
File Name: 变量接收输入.py

@author: lengf
@date: 2025-04-13
@email: lengfo@163.com
@version: 1.0.0
"""


# 使用input()函数接收用户输入并赋值给变量
# 得到的数据类型为字符串
name = input('请输入你的名字：')
print('你好，' + name + '！')
# 若输入的数据类型为整数，则需要使用int()函数将其转换为整数类型
# 如果不是整数样式的输入，，即在int()函数转换时,则会报错
int_num = int(input('请输入一个整数：'))
print('你输入的整数是：' + str(int_num))
# 若输入的数据类型为浮点数，则需要使用float()函数将其转换为浮点数类型
# 如果不是浮点数样式的输入，则在float()函数转换时,则会报错
float_num = float(input('请输入一个浮点数：'))
print('你输入的浮点数是：' + str(float_num))

# 以下代码演示了如何使用input()函数接收多个输入并进行运算
input_str = input('请输入两个数字，用空格分隔：')    # 接收用户输入的字符串，其实是接收了一个字符串（包含空格），后面只是用split()方法将其分割成列表.
num_list = input_str.split()    # 将输入的字符串以空格分隔,字符串的split()方法是将字符串按照空格分隔，并返回一个列表。
a = int(num_list[0])
b = int(num_list[1])
print(a + b)
print(a - b)


# input()函数接收的是一个字符串，
# 如果需要数据转换，则需要使用相应的函数进行转换，如int()、float()等。
# 转换时容易出现错误，如输入的字符串不是整数、浮点数等格式，则转换时会报错。
# 因此，一般处理方法是，使用input()函数接收用户输入，然后使用try-except语句进行异常处理，
# 捕获转换错误，并给出相应的提示信息。
# 如下代码演示了如何使用try-except语句进行异常处理：

while True:
    try:
        num = int(input('请输入一个整数：'))
        print('你输入的整数是：' + str(num))
        break
    except ValueError:
        print('输入的不是整数，请重新输入！')

        
        # 以上代码使用while True循环，直到输入有效整数为止。
