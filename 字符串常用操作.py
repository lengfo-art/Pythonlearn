"""
字符串常用操作
得到长度，首字母大写，变大写，判断是否大写，
判断是否以hello开头，判断是否以hello结尾，
判断是否以感叹号开头，判断是否以感叹号结尾，字符串切片，
字符串拼接，字符串格式化

Version: 0.1
Author: 林风
Date: 2018-02-27
"""

str1 = 'hello，你好呀，My name is 小明，今年18岁。'
print('字符串的长度是:', len(str1))
print('单词首字母大写: ', str1.title())  # 单词首字母大写
print('字符串变大写: ', str1.upper())   # 全部大写，汉字中的字母都变成大写
print(str1.lower())   # 全部小写
print('字符串是不是大写: ', str1.isupper())  # 判断是否全部大写
print('字符串是不是以hello开头: ', str1.startswith('hello')) # 判断是否以hello开头
print('字符串是不是以hello结尾: ', str1.endswith('hello')) # 判断是否以hello结尾
print('字符串是不是以感叹号开头: ', str1.startswith('!')) # 判断是否以感叹号开头
print('字符串是不是句号结尾: ', str1.endswith('。')) # 判断是否以感叹号结尾
str2 = '- \u9a86\u660a'  
str3 = str1.title() + ' ' + str2.lower()
print(str3)

# 字符串其他操作
# 字符串切片
print(str1[0:5])
print(str1[6:11])
print(str1[::-1])
# 字符串拼接
str4 = 'Python'
str5 = 'is'
str6 = 'awesome'
str7 = str4 +'' + str5 +'' + str6
print(str7)
# 字符串格式化
str8 = 'Hello, {0}, 成绩提升了 {1:.2f}%'.format('小明', 17.56789)
print(str8)

