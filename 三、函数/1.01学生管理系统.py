
# --*--coding :utf-8--*--
# @Time : 2023/10/1 16:00
# @Author :  tang
# @File : Student_System.py

import time
import os

# 定义学生信息列表，用于存储学生信息
# 列表中每个学生信息是一个字典，字典中包含学生的姓名、年龄、电话号码等信息
students = []

# 开始提示，输入操作菜单，1.添加学生信息，2.查询学生信息，3.修改学生信息，4.删除学生信息，5.显示所有学生信息，6.退出系统
def start_prompt():
    print("-----欢迎使用学生信息管理系统-----")
    print("1. 添加学生信息")
    print("2. 查询学生信息")
    print("3. 修改学生信息")
    print("4. 删除学生信息")
    print("5. 显示所有学生信息")
    print("6. 退出系统")
    print("---------------------------------")

# 定义函数，添加学生信息
def add_student():
    '''
    添加学生信息函数
    1. 输入学生姓名、年龄、电话号码。
    '''
    student = {} # 创建一个空字典，用于存储学生信息
    student['name'] = input('请输入学生姓名：')
    
    #判断学生信息是否已存在，如果存在则提示用户
    for s in students:
        if s['name'] == student['name']:
            print("学生信息已经存在，请重新输入！")
            return
    student['age'] = input('请输入学生年龄：')
    student['iphone'] = input('请输入学生电话号码：')
    students.append(student) # 将学生信息添加到列表中


# 定义函数，查询学生信息
def search_student():
    '''
    查询学生信息函数
    1. 输入学生姓名，查询学生信息。
    '''
    name = input('请输入要查询的学生姓名:')
    for student in students:
        if student['name'] == name:
            print('学生信息：')
            print('姓名：',student['name'])
            print('年龄：',student['age'])
            print('电话号码 ：',student['iphone'])
            break
    else:
        # 如果没有找到学生信息，则提示用户
        # else语句与for语句配合使用，当for循环正常结束时，执行else语句
        # 当for循环被break语句中断时，不执行else语句
        # 这里是为了避免在for循环中使用break语句后，else语句也被执行的情况
        print('没有找到该学生的信息，请重新输入！')
        return
 


# 定义函数，修改学生信息

def modify_student():
    '''
    修改学生信息函数
    1. 输入学生姓名，查询学生信息。
    2. 输入要修改的学生信息。
    '''
    name = input('请输入要修改的学生姓名：')
    for student in students:
        if student['name'] == name:
            print('当前学生信息：')
            print('姓名：', student['name'])
            print('年龄：', student['age'])
            print('电话号码：', student['iphone'])
            # 输入新的学生信息
            student['name'] = input('请输入新的学生姓名：')
            student['age'] = input('请输入新的学生年龄：')
            student['iphone'] = input('请输入新的学生电话号码：')
            print('学生信息修改成功！') 
            break
    else:
        # 如果没有找到学生信息，则提示用户
        # else语句与for语句配合使用，当for循环正常结束时，执行else语句
        # 当for循环被break语句中断时，不执行else语句
        # 这里是为了避免在for循环中使用break语句后，else语句也被执行的情况
        print('没有找到该学生的信息，请重新输入！')
        return

# 定义函数，删除学生信息
def delete_student():
    '''
    删除学生信息函数
    1. 输入学生姓名，查询学生信息。
    2. 删除学生信息。
    '''
    name = input('请输入要删除的学生姓名:')
    for s in students:
        if s['name'] == name:
            students.remove(s)
            print(f'{name}此学生信息删除成功！')
            break
    else:
        # 如果没有找到学生信息，则提示用户
        # else语句与for语句配合使用，当for循环正常结束时，执行else语句
        # 当for循环被break语句中断时，不执行else语句
        # 这里是为了避免在for循环中使用break语句后，else语句也被执行的情况
        print('没有找到该学生的信息，请重新输入！')
        return


# 定义函数，显示所有学生信息
def show_all_students():
    '''
    显示所有学生信息函数
    1. 显示所有学生信息。
    '''
    if len(students) == 0:
        print('没有学生信息，请先添加学生信息！')
        
        return
    print('所有学生信息：')
    i = 1  # 学生序号
    for s in students:
        print(f'第{i}位：')
        print('姓名：', s['name'])
        print('年龄：', s['age'])
        print('电话号码：',s['iphone'])
        i += 1
        print('--'*20)
        


# 定义函数，退出系统
def exit_system():
    '''
    退出系统函数
    1. 显示退出提示信息。
    '''
    print('感谢使用学生信息管理系统 ！')
    print('系统将在3秒后退出，请稍等...')
    time.sleep(3)  # 等待3秒
    os._exit(0)  # 退出系统
    # 退出系统，os._exit(0)表示正常退出系统，os._exit(1)表示异常退出系统


# 主函数，循环显示操作菜单，等待用户输入操作


def main():
    while True:
        print("欢迎使用学生信息管理系统")
        print("1. 添加学生信息")
        print("2. 查询学生信息")
        print("3. 修改学生信息")
        print("4. 删除学生信息")
        print("5. 显示所有学生信息")
        print("6. 退出系统")
        choice = input("请输入您的选择：")
        match choice:
            case '1':
                add_student()
            case '2':
                search_student()
            case '3':
                modify_student()
            case '4':
                delete_student()
            case '5':
                show_all_students()
            case '6':
                exit_system()
            
      


main()  # 调用主函数，开始程序