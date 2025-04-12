"""
将华氏温度转换为摄氏温度
F 为华氏度，C 为摄氏度。
F = 1.8C + 32
C = (F - 32) / 1.8

调整字符串格式化输出的语法，使其更加简洁
增加相互转换功能。

Version: 0.2

Version: 0.1
Author: 林风
Date: 2025-04-10
"""

# f = float(input('请输入华氏温度: '))
# c = (f - 32) / 1.8
# print('%.1f华氏度 = %.1f摄氏度' % (f, c))

# print(f'{f}华氏度 = {c :.1f}摄氏度') # 字符串格式化输出

print('这是一个华氏温度和摄氏温度相互转换的功能:')
# 相互转换功能

def f_to_c(f):
    '''
    华氏度转摄氏度
    :param f: 华氏度
    :return: 摄氏度
    '''
    c = (f - 32) / 1.8
    return c

def c_to_f(c):
    '''
    摄氏度转华氏度
    :param c: 摄氏度
    :return: 华氏度
    '''
    f = c * 1.8 + 32
    return f

    
def main():
    '''
    主函数
    :return: None
    '''
    # 使用match语法
    while True:
        try:
            chose: int = int(input('请输入要进行的操作：\n 1、华氏度转摄氏度\n 2、摄氏度转华氏度\n 3、退出\n'))
            match chose:
                case 1:
                    f = float(input('请输入华氏度:'))
                    c = f_to_c(f)
                    print(f'{f}华氏度 = {c:.2f}摄氏度')
                    continue
                case 2:
                    c = float(input('请输入摄氏度:'))
                    f = c_to_f(c)
                    print(f'{c:.2f}摄氏度 = {f}华氏度')
                    continue
                case 3:
                    break
                case _:
                    print('输入错误，请重新输入！')
                    continue    
        except ValueError:
            print('输入错误，请重新输入！')
        

if __name__ == '__main__':
    main()