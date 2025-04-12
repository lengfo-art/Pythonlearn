# -*- coding: utf-8 -*-

'''
模块名称：代码编写的约定
文件描述：记录一些python 代码编写的约定 
文件作者：林风  
创建日期：2025-04-10
'''

# 下面是python代码编写的约定：

# 1. 缩进：每级缩进使用 4个空格（不用 Tab）
# 续行应与包裹元素对齐（垂直对齐或悬挂缩进）
def long_function_name(
        var_one, var_two,
        var_three, var_four):
    print(var_one)

# 2. 命名规范
#  变量/函数：小写字母 + 下划线（snake_case）
student_name = "张三"
def calculate_total():
    pass

#  类名：首字母大写的驼峰式（CamelCase）
class UserAccount:
    pass

# 常量：全大写 + 下划线
MAX_CONNECTIONS = 100

# 4. 空格使用
# 运算符两侧、逗号后加空格

x = 3 + 1
list = [1, 2, 3]

# 函数/类定义前后空两行，方法定义空一行：

class MyClass:
    
    def method_one(self):
        pass
        
    def method_two(self):
        pass


# 5. 注释
# 行注释用 # 后接1个空格
# 文档字符串（docstring）用三引号，遵循 PEP 257：

def calculate(a, b):
    """返回两个数的和
    
    Args:
        a (int): 第一个参数
        b (int): 第二个参数
        
    Returns:
        int: 计算结果
    """
    return a + b


# 6. 导入规范
# 按标准库 → 第三方库 → 本地库分组，每组空一行
# 每行导入一个模块：

# import os
# import sys

# import numpy as np
# import pandas as pd

# from my_module import MyClass

# 7. 其他
# 避免使用 ; 将多语句写在一行
# 使用 is/is not 判断 None，而非 ==
# 用 ''.startswith() 代替字符串切片检查前缀
# 避免使用 eval() 函数，而使用 ast.literal_eval() 函数
# 避免使用 exec() 函数，而使用 ast.parse() 函数

# 4. 文档字符串：模块、类、函数的第一行应该是文档字符串，描述模块、类、函数的功能。

# 9. 注释：注释应该使用英文，并以句号结尾。

# 11. 文档测试：编写代码时，应该先编写文档测试，即编写一个测试用例，验证代码的正确性。

# 12. 异常处理：使用try-except语句处理异常。

# 13. 格式化字符串：使用f-string（Python 3.6+ 推荐方式）
# print(f"姓名：{name}，年龄：{age}")

# 15. 编码：使用utf-8编码。