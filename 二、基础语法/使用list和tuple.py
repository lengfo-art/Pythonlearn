# 都是一种可迭代对象

# * 可迭代对象有以下几种：
# 1. 字符串，可包含各种字符。
# 2. 列表，可包含各种类型数据 。
# 3. 下标，（索引），切片与字符串一样。
# 4. 元组，不可修改的序列。
# 5. 集合，无序不重复的元素的集合。
# 6. 字典，键值对的集合。
# 7. range，可迭代对象，生成一个序列的数字。
# 8. iter，可迭代对象，生成一个迭代器。




import random


for i in 'abc':
    print(i) # 字符串是可迭代对象
for i in [1,2,3]:
    print(i) # 列表是可迭代对象
for i in (1,2,3):
    print(i)
    # 元组是可迭代对象
for i in {1,2,3}:
    print(i)
# 集合是可迭代对象
for i in {1:'a',2:'b',3:'c'}:
    print(i)
    # 字典是可迭代对象
for i in range(5):
    print(i)
    # range是可迭代对象
for i in iter('abc'):
    print(i)
    # iter是可迭代对象
for i in iter([1,2,3]):
    print(i)
    # iter是可迭代对象
    # iter是自定义的可迭代对象

class MyIter:
    def __init__(self,data):
        self.data = data
        self.index = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        result = self.data[self.index]
        self.index += 1
        return result

# 2. 列表，可包含各种类型数据 。
# 3. 下标，（索引），切片与字符串一样。
# 4. 列表方法

    # 1. append   #一次只能添加一次值，且只添加在末尾
    # 2. extend  #方法把其参数按各项值插入列表其后，

    
list1=[1,2]
list1.extend([5,6])
print(list1) # [1, 2, 5, 6] # extend方法可以添加任意类型的元素
list1.extend('abc') # type: ignore # 空列表也可以使用extend方法
print(list1) # [1, 2, 5, 6, 'a', 'b', 'c'] 
# 5. index  返回参数的索引位置，


list1=[1,2,3,4,5]
print(list1.index(3)) # 2 # 返回元素3的索引位置
print(list1.index(3,1,4)) # 2 # 返回元素3的索引位置，范围在1到4之间
# index(value,start,end)
# 1. value：要查找的元素。
# 2. start：可选参数，指定查找的起始索引位置，默认为0。
# 3. end：可选参数，指定查找的结束索引位置，默认为列表的长度。

    # insert方法
str_data = ['one', 'two', 'three']
str_data.insert(1, 'four') # 在索引1的位置插入元素'four'
print(str_data) # ['one', 'four', 'two', 'three']

# 7. 列表的数据修改

   
str_data[1]='five' # 修改索引1位置的元素为'five'
print(str_data) # ['one', 'five', 'two', 'three']


# 8. 数据查询

#     1. in   成员运算符，返回布尔值，`
boo='one' in str_data    # 判断元素是否在列表中  # True`
#     2. not in    `
bo  = 'one' not in str_data # 判断元素是否不在列表中  # False`
#     3. count   `
count = str_data.count('one') # 统计元素在列表中出现的次数  # 1`

# 9. 删除元素    del,    remove  ,pop,  clear.

li=['name','city','age','hobby']
del li[1] # 删除索引1位置的元素
print(li) # ['name', 'age', 'hobby'] # 删除索引1位置的元素
li.remove('age') # 删除元素'age'
print(li) # ['name', 'hobby'] # 删除元素'age'

po = li.pop(1) # 删除索引0位置的元素 hobby 并返回该元素
li.clear() # 清空列表
print(li) # [] 
del li
# print(li) #  # NameError: name 'li' is not defined # 删除整个列表

       

list1 = [8,2,6,1,5]
list1.reverse() # 反转列表
print(list1) # [5, 1, 6, 2, 8] # 反转列表
 


# 列表排序
list2 = [1,3,4,2,5]
list2.sort(reverse=True) # 降序排序
print(list2) # [5, 4, 3, 2, 1] # 降序排序
list2.sort() # 升序排序
print(list2) # [1, 2, 3, 4, 5] # 升序排序

# 11. 列表嵌套

#      1. 例子电影，（声音，画面，时间轴）三维数组。
#      2. 音乐，（声音，时间轴）二维数据
#      3.


#定义办公室
office = [[],[],[]] # 创建一个三维列表

# 定义老师
names = ['张三','李四','王五','赵明','bingbing','tom'] # 老师姓名

# 对当前老师列表进行迭代
for name in names:
    random_num = random.randint(0,2) # 随机生成一个0-2之间的整数
    office[random_num].append(name) # 将老师姓名添加到对应的办公室列表中
    
i = 1 # 定义一个变量i，用于输出办公室的编号
for office_name in office: # 对办公室列表进行迭代
    print(f'办公室{i}的人数为：{len(office_name)}') # 输出办公室的编号和人数
    i+=1 # 将i加1
    for name in office_name: # 对办公室中的老师姓名进行迭代
        print(name) # 输出老师姓名
    print('-'*40) # 输出分隔线


# randint 用法
# random.randint(a, b) # 返回一个随机整数 N，使得 a <= N <= b。
