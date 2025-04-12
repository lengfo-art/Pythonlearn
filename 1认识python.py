"""
检查变量的类型

Version: 0.1
Author: 骆昊
Date: 2018-02-27
"""

'''
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
'''

import turtle  # 导入turtle绘图库

# 设置画笔宽度为4
turtle.pensize(4)
# 设置画笔颜色为红色
turtle.pencolor('red')

# 向前移动100个单位长度
turtle.forward(100) 
# 右转90度
turtle.right(90)

# 再次向前移动100个单位长度
turtle.forward(100)
# 右转90度
turtle.right(90)

# 继续向前移动100个单位长度
turtle.forward(100)
# 再次右转90度
turtle.right(90)

# 最后一次向前移动100个单位长度
turtle.forward(100)
# 进入主循环等待用户操作（保持窗口打开）
turtle.mainloop()