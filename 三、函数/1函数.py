# 1. 函数声明

#     1. def 关键字， def func(args):

#     # 定义根据PI计算面积函数
def area_of_circle(radius):
    '''
    计算圆的面积
    :param radius: 圆的半径
    :return: 圆的面积
#         '''
#     ```

# from .hello import *    

#     
if __name__ == '__main__':# 如果该文件是主程序，则执行以下代码
    pass

#         ```
# 4. 可有reture   返回，可有多个返回值，

#     1. ` return area , PI   # 返回圆的面积和PI  ,返回的是一个元组，`
# help(quadratic)  # 查看函数说明文档`
# 6. 形参，实参
# 7. 默认参数
# 8. 如函数中没有reture语句，则会自动加上，reture None     即返回None值
# 9. ```python
def add_num(a, b):
    return a + b  # 返回两个数的和

f = add_num(1, 2) # 调用函数，传入参数1和2
print(f,type(f)) # 返回函数值，和函数返回结果的类型，
        # reture 语句有多个结果返回，则的类型为元组，元组的类型为<class 'tuple'>，因type的参数是函数返回值
        # 其他按具体设定类型，函数可以返回任何 Python 对象，常见类型包括：简单类型：int, float, str, bool, None；容器类型：list, tuple, dict, set
        # 自定义类型：类的实例、函数对象（function）、模块等
print(add_num.__code__.co_argcount) # 返回函数的参数个数，函数参数个数为2
print(add_num(1, 2),type(add_num)) # 返回两个数的和及函数类型，函数类型为<class 'function'>，因type的参数是函数对象
print(add_num.__code__) # 返回函数的代码对象
print(add_num.__name__) # 返回函数名称
print(add_num.__doc__) # 返回函数的文档字符串
#     ```

# 	函数的方法。

# 10. 自定义函数有四种类型：

#      1. 无参数无返回值    应该是有返回语句，无reture 语句则会自动加 reture None
#      2. 无参数有返回值
#      3. 有参数无返回值
#      4. 有参数有返回值


# 11. 函数内部定义的变量具有隔离性，即局部变量。

#      1. global   ，如果想使用别的局部变量，可用blobal.
#      2.

# 12. 函数嵌套调用

# ```python
# fu = func1  # 把函数func1赋值给变量fu ，fu是一个函数对象，接收的是一个函数对象的地址
# fu()  # 调用函数fu，实际上是调用func1
# func3(fu)  # 调用函数func3，传入fu作为参数

def test_3():
    print('test_3')
    
    

def test_1(func_obj):
    func_obj()  # 调用传入的函数对象
    print('test_1')
    

def test_2():
    print('test_2')
    return test_1  # 返回函数对象test_1

func_obj_attr = test_2()  # 调用test_2，返回函数对象test_1   ,并赋值给func_obj_attr
func_obj_attr(test_3)    # 调用func_obj_attr,即上面被赋给的函数对象test_1   调用test_1，其要且传入了test_3作为参数

# >》》》
# test_2
# test_3
# test_1
# ```

# 13. `print(func1)  # <function func1 at 0x...># 这是函数内存地址`

#      1. `print(id(func1))  # 打印函数func1的地址  #这是函数的地址  十进制`
#      2. `print(id(func1()))# 这是返回值的地址`


# 14. ```python
#      def test_1():
#          print('test_1')
         
         
#      def test_2():
#          print('test_2')
#          return test_1  # 返回函数对象test_1

#      func_obj = test_2()  # 调用test_2，返回函数对象test_1   ,并赋值给func_obj
#      # func_obj()  # 调用func_obj，实际上是调用test_1

#      def test_3(obj):   # obj是一个函数对象,一个形参，可接收任意对象，包括函数对象
#          print('test_3')
#          obj()  # 调用传入的函数对象
         
         
         
#      test_3(func_obj)  # 调用test_3，传入func_obj作为参数，这里传入的是函数对象test_1的地址
#      # test_3(test_1)  # 直接传入函数对象test_1作为参数，，效果一样

#      》》》
#      test_2
#      test_3
#      test_1
#      ```

# 15. 函数递归调用

#      1. ```python
def factorial(n):
    '''
    计算阶乘的递归函数
    n! = n * (n-1)!
    0! = 1
    1! = 1
    2! = 2 * 1! = 2 * 1 = 2
    如果 n < 0，返回 None
    如果 n == 0 或 n == 1，返回 1
    否则返回 n * factorial(n - 1),
    
    '''
    if n == 0 or n == 1:
        return 1           #    递归终止条件，
    else:
        return n * factorial(n - 1)  # 递归调用
#                  # 递归调用，首先返回 n * factorial(n - 1)，而其中的factorial(n - 1)又会调用自身，
#                  # 即函数体内又调用了自身，形成递归调用，
#                  # 直到n=0或n=1为止,，必须要有终止条件，否则会导致无限递归调用，栈溢出。
#                  # 递归调用的过程是从上到下的，先执行完函数体内的代码，然后再返回结果。
#                  # 到达终止条件后，返回1，然后逐层退出递归调用，即逐层执行完函数体，最终返回结果。
#          ```