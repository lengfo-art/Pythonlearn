# -*- coding: utf-8 -*-
"""
File Name: 字符串操作.py

@author: lengf
@date: 2025-04-13
@email: lengfo@163.com
@version: 1.0.0
"""


# 字符串操作
# 字符串的长度、首字母大写、变大写、是否大写、是否以hello开头、是否以hello结尾、是否以感叹号开头、是否以感叹号结尾、字符串拼接


str1 = 'hello, world!'
print('字符串的长度是:', len(str1))     # 字符串的长度
print('首字母大写: ', str1.capitalize())    # 首字母大写
print('单词首字母大写: ', str1.title())    # 单词首字母大写
print('字符串变大写: ', str1.upper())        # 字符串变大写
print('字符串变小写: ', str1.lower())        # 字符串变小写
# str1 = str1.upper()
print('字符串是不是大写: ', str1.isupper())       # 字符串是不是大写
print('字符串是不是以hello开头: ', str1.startswith('hello'))     # 字符串是不是以hello开头
print('字符串是不是以hello结尾: ', str1.endswith('hello'))     # 字符串是不是以hello结尾
print('字符串是不是以感叹号开头: ', str1.startswith('!'))       # 字符串是不是以感叹号开头
print('字符串是不是一感叹号结尾: ', str1.endswith('!'))       # 字符串是不是以感叹号结尾
str2 = '- \u9a86\u660a'                 # 包含中文的字符串
str3 = str1.title() + ' ' + str2.lower()          # 字符串拼接
print(str3)         # 输出：Hello, World! - 你好
