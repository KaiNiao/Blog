# Python的import用法

本身觉得import很简单，没想到有一天使用的时候各种出错，浪费了好长时间，因此决定好好学习下import的使用。关于模块导入的原理，本篇暂不涉及，过段时间学习。

## 概念

导入（import）的官方定义是Python code in one module gains access to the code in another module by the process of importing it.

模块导入时会在目录中自动新建文件夹__pycache__，其中包含module_name.cpython-36.pyc字节码文件作为缓存，以加快py文件的解释速度。

### 模块与包

导入与两个概念有关，分别是模块与包。

- 模块（module）：本质就是*.py文件，用来从逻辑（实现一个功能）上组织Python代码（变量、函数、类）。
- 包（package）：本质就是一个有层次的文件目录结构（必须带有一个__init__.py文件），定义了一个由模块和子包组成的Python应用程序执行环境。比如一个模块的名称是A.B，那么它表示一个包A中的子模块B。在导入包时，python会从sys.path中的目录来寻找这个包中包含的子目录。

引用内部文件的包名。



### 导入语法

导入的语法分多种，除了以下三种，还可以使用as语法起别名。

- import：可以导入模块或函数。
- from ... import ...：从模块中导入一个指定的部分或从包中导入模块到当前**命名空间**中。
- from ... import *： 导入一个模块的所有内容或从包中导入所有模块。__init__.py文件的__all__列表内容代表 * 号能够匹配到的资源，因此可以在导入时，定义__all__变量对可导入内容进行限制。



### 导入路径

路径的描述可以分为两种，

- 相对导入：指定资源相对于当前位置导入，即导入语句所在的位置。
- 绝对导入：



### 模块启动方式

py文件（模块）的启动方式分两种，**模块直接运行与作为脚本运行**。通过不同方式启动同一文件，sys.path属性的值有何不同。sys.path相当于Linux中的PATH。Python解析器会在这些目录下去寻找依赖库。语法如下：

- python module_name.py：模块直接运行，将把py文件所在的目录放到了sys.path属性中；
- python -m module_name：模块作为脚本运行，将输入命令的目录（也就是当前路径），放到了sys.path属性中，并将自动设置包信息（__package__变量）。官方定义是run library module as a script (terminates option list)。

随后在分别测试绝对导入与相对导入时，均会先后使用两种模块的启动方式。

## 被导入模块

### 文件结构

文件结构如图所示，其中`module_1.py`文件将作为模块在同级目录文件`module_2.py`中进行导入。

这里有一个坑，`module_1.py`文件作为模块使用时，要求**模块包不能以数字开头命名**，否则会报错，报错信息为`SyntaxError: invalid token`，表示导入的包或模块不符合程序命名要求。

### 代码

~~~python
# module_1.py

def func_1():
    print('Module:', __name__)  # 获取模块名
    print('Package:', __package__)
    print('File Path:', __file__)  # 获取文件路径
    # print('Func:', inspect.stack()[1][3])  # 获取函数名
~~~

### 运行结果

模块直接运行与作为脚本启动时，__name__变量都是__main__，__package__变量分别是None与subpackage_1，此外__file__也不同。

~~~bash
(py35) G:\NewYear\code\blog\code>python subpackage_1/module_1.py
Module: __main__
Package: None
File Path: subpackage_1/module_1.py

(py35) G:\NewYear\code\blog\code>python -m subpackage_1.module_1
__init__.__name__: subpackage_1
Module: __main__
Package: subpackage_1
File Path: G:\NewYear\code\blog\code\subpackage_1\module_1.py
~~~

## 导入模块

在同级目录中的module_2.py文件中导入module_1.py。目前subpackage_1文件夹中没有__init__.py文件。

### 部分代码

~~~python
# module_1.py

import sys
print('module_2 path:', sys.path)
print('module_2 name:', __name__)
print('module_2 Package:', __package__)
print('====== import ======')

# 随后使用不同的语法测试不同的模块导入方法
~~~

### import module_1

#### 代码

~~~python
import module_1  # 等价于from module_1 import func_1
module_1.func_1()
~~~

#### 运行结果

~~~bash
(py35) G:\NewYear\code\blog\code>python subpackage_1/module_2.py
module_2 path: ['G:\\NewYear\\code\\blog\\code\\subpackage_1', 'F:\\Anaconda\\envs\\py35\\python35.zip', 'F:\\Anaconda\\envs\\py35\\DLLs', 'F:\\Anaconda\\envs\\py3
5\\lib', 'F:\\Anaconda\\envs\\py35', 'F:\\Anaconda\\envs\\py35\\lib\\site-packages']
module_2 name: __main__
module_2 Package: None
====== import ======
Module: module_1
Package:
File Path: G:\NewYear\code\blog\code\subpackage_1\module_1.py

(py35) G:\NewYear\code\blog\code>python -m subpackage_1.module_2
module_2 path: ['', 'F:\\Anaconda\\envs\\py35\\python35.zip', 'F:\\Anaconda\\envs\\py35\\DLLs', 'F:\\Anaconda\\envs\\py35\\lib', 'F:\\Anaconda\\envs\\py35', 'F:\\A
naconda\\envs\\py35\\lib\\site-packages']
module_2 name: __main__
module_2 Package: subpackage_1
====== import ======
Traceback (most recent call last):
  File "F:\Anaconda\envs\py35\lib\runpy.py", line 193, in _run_module_as_main
    "__main__", mod_spec)
ImportError: No module named 'module_1'
~~~

#### 分析

- from module_1 import func_1正常，效果等价于import module_1；
- import module_1.func_1报错，ModuleNotFoundError: No module named 'module_1.func_1'; 'module_1' is not a package。



### import module_1.func_1

#### 代码

~~~python
from module_1 import func_1
func_1()
~~~

#### 运行结果





