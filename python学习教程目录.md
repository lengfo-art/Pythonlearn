以下是一份**Python学习记录**，主要以瘳雪峰的《Python教程》为学习顺序，构建目录，记录多以 .py文件形式形成，尽量多手打输入代码，注释详尽清晰，提高学习效果。

结合从github，clone来的 《Python - 100天从新手到大师》的教程，参照其中示例和练习，坚持修改完善代码，加深所学知识点。

---

### **Python** 

#### 一、初识Python

1. 简介
2. 历史
3. 安装
4. 第一个程序

#### **二、Python基础语法**

1. **变量与数据类型**
2. - 基本数据类型：`int`, `float`, `str`, `bool`
   - 类型转换与检查（`type()`, `isinstance()`）
   - 变量命名规则与动态类型特性
3. **运算符与表达式**

   - 算术运算符（`+`, `-`, `*`, `/`, `//`, `%`, `**`）
   - 比较运算符（`==`, `!=`, `>`, `<`）
   - 逻辑运算符（`and`, `or`, `not`）
   - 赋值运算符（`=`, `+=`, `-=`）
4. **流程控制**

   - 条件语句：`if-elif-else`（含三元表达式）
   - 循环语句：`while`循环、`for`循环（含 `range()`）
   - 循环控制：`break`, `continue`, `pass`
5. **函数基础**

   - 函数定义与调用
   - 参数传递（位置参数、关键字参数、默认参数）
   - 返回值与 `None`
   - 局部变量与全局变量（`global`关键字）

---

#### **第二阶段：核心数据结构**

6. **列表（List）**

   - 列表的增删改查（`append()`, `remove()`, `slice`）
   - 列表推导式与生成器表达式
   - 常用方法：`sort()`, `reverse()`, `copy()`
7. **元组（Tuple）**

   - 不可变特性与应用场景
   - 元组解包与命名元组（`collections.namedtuple`）
8. **字典（Dict）**

   - 键值对操作（`keys()`, `values()`, `items()`）
   - 字典推导式
   - 默认字典（`defaultdict`）与有序字典（`OrderedDict`）
9. **集合（Set）**

   - 去重与集合运算（`union`, `intersection`, `difference`）
   - 不可变集合（`frozenset`）
10. **字符串（String）**

    - 字符串格式化（f-string、`format()`）
    - 常用方法：`split()`, `join()`, `strip()`
    - 正则表达式基础（`re`模块）

---

#### **第三阶段：函数与高级特性**

11. **函数进阶**

    - 可变参数（`*args`, `**kwargs`）
    - 匿名函数（`lambda`）
    - 闭包与装饰器（`@decorator`）
    - 作用域与 `nonlocal`关键字
12. **生成器与迭代器**

    - 迭代器协议（`__iter__`, `__next__`）
    - 生成器函数（`yield`）
    - 生成器表达式
13. **错误与异常处理**

    - 常见异常类型（`ValueError`, `TypeError`, `IndexError`）
    - `try-except-finally`结构
    - 自定义异常（继承 `Exception`）
14. **文件与IO操作**

    - 文件读写（文本模式与二进制模式）
    - 上下文管理器（`with`语句）
    - `os`与 `pathlib`模块（路径操作）

---

#### **第四阶段：面向对象编程（OOP）**

15. **类与对象**

    - 类定义与实例化
    - 属性（实例属性、类属性）与方法
    - `self`关键字与 `__init__`方法
16. **面向对象三大特性**

    - **封装**：私有属性（`_name`, `__name`）与 `@property`
    - **继承**：单继承、多继承（`super()`）
    - **多态**：方法重写与鸭子类型
17. **魔术方法**

    - `__str__` vs `__repr__`
    - 算术操作符重载（`__add__`, `__eq__`）
    - 上下文管理（`__enter__`, `__exit__`）
18. **抽象基类（ABC）**

    - `abc`模块与 `@abstractmethod`
    - 接口设计实践

---

#### **第五阶段：模块化与工程化**

19. **模块与包**

    - 模块导入（`import`, `from...import`）
    - `__name__`与 `__main__`
    - 包的创建与 `__init__.py`
20. **标准库常用模块**

    - `datetime`（时间处理）
    - `json`/`pickle`（序列化）
    - `random`（随机数生成）
    - `collections`（高级数据结构）
21. **第三方库管理**

    - `pip`安装与 `requirements.txt`
    - 虚拟环境（`venv`, `conda`）
22. **代码规范与测试**

    - PEP 8编码规范
    - 单元测试（`unittest`, `pytest`）
    - 调试技巧（`pdb`, IDE调试器）

---

#### **第六阶段：高级应用与实战**

23. **并发编程**

    - 多线程（`threading`）与GIL限制
    - 多进程（`multiprocessing`）
    - 异步IO（`asyncio`）
24. **网络编程**

    - Socket编程基础
    - HTTP请求（`requests`库）
    - REST API设计与 `Flask`快速入门
25. **数据处理与分析**

    - `NumPy`数组操作
    - `Pandas`数据处理（DataFrame）
    - `Matplotlib`/`Seaborn`可视化
26. **数据库操作**

    - SQLite3基础
    - ORM框架（`SQLAlchemy`）
    - NoSQL（`MongoDB`与 `pymongo`）
27. **自动化与爬虫**

    - `BeautifulSoup`/`Scrapy`爬虫
    - `Selenium`自动化测试
28. **Web开发进阶**

    - Django框架核心概念（MTV模式）
    - FastAPI构建高性能API
29. **机器学习入门**

    - `Scikit-learn`基础（分类、回归）
    - 深度学习框架（`TensorFlow`/`PyTorch`简介）

---

#### **第七阶段：项目实战与优化**

30. **实战项目推荐**

    - **初级**：
      - 命令行待办事项工具
      - 天气查询脚本（API调用）
    - **中级**：
      - Flask博客系统
      - 数据分析报告生成器
    - **高级**：
      - 电商爬虫+数据分析
      - 基于FastAPI的在线考试系统
31. **性能优化**

    - 代码性能分析（`timeit`, `cProfile`）
    - 内存管理（`gc`模块）
    - Cython加速关键代码
32. **部署与DevOps**

    - Docker容器化
    - CI/CD流程（GitHub Actions）
    - 云服务部署（AWS/Aliyun）

---

### **学习资源推荐**

- **书籍**：
  - 入门：《Python Crash Course》
  - 进阶：《流畅的Python》《Effective Python》
- **网站**：
  - 官方文档：[docs.python.org](https://docs.python.org/3/)
  - 实战平台：[LeetCode](https://leetcode.com/)、[Real Python](https://realpython.com/)
- **视频**：
  - B站：廖雪峰Python教程、Corey Schafer系列
  - Coursera：Python for Everybody

---

### **学习路线建议**

1. **基础阶段**（1-2周）：掌握变量、函数、流程控制。
2. **核心阶段**（3-4周）：深入数据结构、OOP、模块化。
3. **进阶阶段**（4-6周）：选择方向（Web/数据分析/AI）并实战。
4. **持续提升**：参与开源项目，学习设计模式与架构。
