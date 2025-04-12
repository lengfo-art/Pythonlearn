"""
运算符的使用
加注释

Version: 0.1
Author: 林风    
Date: 2025-04-10
"""

a = 5 # 赋值运算符
b = 10  # 赋值运算符
c = 3  # 赋值运算符
d = 4  # 赋值运算符
e = 5  # 赋值运算符
a = a + b  # 加法运算符
e = 5    # 赋值运算符
a += b   # 加法赋值运算符
a -= c   # 减法赋值运算符
a *= d   # 乘法赋值运算符
a /= e   # 除法赋值运算符
a //= e  # 整除赋值运算符  取商后舍弃小数的部分
a %= e   # 取模赋值运算符  取余数
a **= e  # 幂赋值运算符
print("a = ", a)


flag1 = 3 > 2  # 比较运算符  True
flag2 = 2 < 1  # 比较运算符  False
flag3 = flag1 and flag2  # 逻辑运算符  与运算False
flag4 = flag1 or flag2  # 逻辑运算符    或运算True
flag5 = not flag1  # 逻辑运算符    非运算False
print("flag1 = ", flag1)  
print("flag2 = ", flag2)
print("flag3 = ", flag3)
print("flag4 = ", flag4)
print("flag5 = ", flag5)
print(flag1 is True)    # 身份运算符 
print(flag2 is False)   # 身份运算符    
print(flag2 is not False)    # 身份运算符