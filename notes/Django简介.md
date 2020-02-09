# Django 简介（一）

Django是一种基于Python的Web开发框架。

那么，什么是Web开发？Web开发指的是开发基于B/S架构，通过前后端的配合，将后台服务器的数据在浏览器上展现给前台用户的应用。

参考[刘江老师的Django2.2教程](https://www.liujiangblog.com/)，该教程中对Django的使用进行了系统的讲解。为加深自己的理解，本文对相关知识点进行总结。

### Web 框架

全栈框架是指除了封装网络和线程操作，还提供HTTP、数据库读写管理、HTML模板引擎等一系列功能的Web框架，比如Django、Tornado和Flask。一般Web框架的架构：

![84-1.png](http://liujiangblog.com/static/images/course/84-1.png)

软件设计理念

- MVC，将业务逻辑（Controller，控制器）、数据（Model，模型）、界面（View，视图）分离，实现解耦；
- MTV，本质类似，三者分别为模型（Model，ORM）、模板（Template）、视图（View，负责业务逻辑）。Django满足MTV，还有一个URL分发器。Django的MTV模型组织可参考下图所示：

![image](http://liujiangblog.com/static/images/course/84-3.png)



Django应用



### Django Shell

Python交互式命令行程序，自动引入了项目环境，可使用它与项目进行交互使用。



### 通用视图

使用通用视图：减少重复代码

上面的detail、index和results视图的代码非常相似，有点冗余，这是一个程序猿不能忍受的。他们都具有类似的业务逻辑，实现类似的功能：通过从URL传递过来的参数去数据库查询数据，加载一个模板，利用刚才的数据渲染模板，返回这个模板。由于这个过程是如此的常见，Django很善解人意的帮你想办法偷懒，于是它提供了一种快捷方式，名为“通用视图”。



### 对象关系映射 ORM

O（objects）：类和对象。R（Relation）：关系，关系数据库中的表格。M（Mapping）：映射。

ORM将一个Python的对象映射为数据库中的一张关系表。它将SQL封装起来，程序员不再需要关心数据库的具体操作，只需要专注于自己本身代码和业务逻辑的实现。

于是，整体的实现过程就是：Python代码，通过ORM转换成SQL语句，再通过pymysql去实际操作数据库。最典型的ORM就是SQLAlchemy了，而**Django自带ORM系统，不需要额外安装别的ORM。**ORM中一个Python的类，就是一个模型，代表数据库中的一张数据表。

![image.png-18.7kB](http://static.zybuluo.com/feixuelove1009/k1s4q20bnmdy1pbn0lxie992/image.png)



### 流程 demo

创建mysite项目，创建polls应用，创建Question与Choice模型。

1. 创建项目

创建django项目：django-admin startproject mysite

启动服务，用于访问：python manage.py runserver 8080，默认8000

主目录文件（**名称与项目名称相同**）：

- __init__.py：项目初始化文件，服务器启动时自动执行。默认为空；
- urls.py：项目基础url（路由）配置文件；
- wsgi.py：应用服务器配置文件；
- settings.py：项目主设置文件。

其中settings.py 内容：

- BASE_DIR：获取当前项目的根目录绝对路径；
- ALLOW_HOSTS：设置允许访问本项目的的地址列表，默认本机localhost访问，"*"表示局域网可访问；
- INSTALLED_APPS：已安装的应用，自定义应用时需要进行注册。DRF也需要注册；
- MIDDLEWARE：指定注册的中间件；
- ROOT_URLCONF：指定项目的基础路由配置文件。

URL配置：

如果页面很多，都写在根urls.py中就很乱。于是，在根urls.py中引入include，在APP目录下创建urls.py文件，格式与根urls.py相同。 

2. 创建应用

 创建应用（项目）：python manage.py startapp polls。

同时在setting.py中INSTALLED_APPS中进行注册。

应用中没有主路由配置文件urls.py，需要创建子路由配置文件，使用include在主路由中导入子路由进行分发，这样可以实现从主路由-->子路由-->视图的指向。

应用指的就是网站中一个独立的程序模块， 主目录一般不处理用户的具体请求，主目录主要做项目的初始化与设置，以及请求的分发。 

应用的结构组成：

- migration目录：数据库中间文件（日志文件），模型中使用；
- __init__.py：应用初始化文件；
- admin.py：应用后台管理配置文件；
- apps.py：应用的属性配置文件；
- models.py：模型文件，与数据库有关。使用ORM框架 ；
- tests.py：测试模块；
- views.py：定义视图的文件；

3. 数据库迁移

- 生成迁移（sql语句）：python manage.py makemigrations；

- 执行迁移：python manage.py migrate

创建数据库表，保存save()

4. 项目目录



## 模型层 Models

### 基础

创建数据库，完成配置，模型类写好以后进行数据库的同步，修改表结构时要在模型类中进行修改，并生成新的中间文件。**表名中会自动添加应用名**，如index_books。

在应用根目录下models.py中引入models模块。创建类，继承models.Model，该类即是一张数据表。在类中创建字段。

Models中的每个class都称为模型类（Model类）或实体类（Entry/Entity）；

Models中的每个模型类都必须继承自models.Model，进而可以实现映射与CRUD。

Entry.objects 是包含了模型对象的实例，QuerySet 是模型对象。

应用的views.py文件中导入models.py，插入数据有三种方式。

通过ORM向db中查询数据是通过Entry.objects调用查询接口，返回QuerySet查询结果集。 

常用数据库迁移命令：

- python manage.py makemigrations：将每个应用下的models.py文件生成一个数据库的中间文件，并保存在migrations目录中；
- python manage.py migrate：将每个应用下的migrations目录的新的中间文件同步到数据库中，实现映射， django中默认有部分与后台管理相关的中间文件，可以通过映射进行显示。每次对模型进行增、删、修改时，请务必执行命令python manage.py migrate，让操作实际应用到数据库上。这里可以选择在执行migrate之前，先执行python manage.py makemigrations让修改动作保存到记录文件中，方便github等工具的使用。
- 报错django.db.migrations.exceptions.[InconsistentMigrationHistory](https://www.cnblogs.com/WoLykos/p/8886900.html)
- 数据的版本切换：python manage.py migrate index 0001，执行应用中版本号对应的中间文件，恢复到0001版本号；
- 通过数据库自动导出models.py：python manage.py inspectdb > 文件名.py，将表映射为类。

### 关系类型字段

包括多对一、多对多、一对一，其中多对一最常见，多对多默认会创建第三张关系表。

多对一（ForeignKey）多对一的关系，通常被称为外键。外键需要两个位置参数，一个是关联的模型，另一个是`on_delete`选项。根据Django模型的定义原则，**外键要定义在‘多’的一方！**，默认情况下，外键都是关联到被关联对象的主键上（一般为id）。在实际的数据库后台，Django会为每一个外键添加`_id`后缀，并以此创建数据表里的一列。

关系的对象

正向关联对象有一个，反向关联对象有多个。正向关联即为有外键的表去关联查询对应的表，反向关联即为无外键的表去关联查询其他有该表外键的表。如一张问卷有多个问题，在问题Question模型类中设置问卷Choice外键，根据问题查询所属问卷为正向关联，根据问卷查询所有问题为反向关联。如果一个模型有ForeignKey，那么该ForeignKey所指向的外键模型的实例可以通过一个管理器进行反向查询，返回源模型的所有实例。默认情况下，这个管理器的名字为`FOO_set`，其中FOO是源模型的小写名称。可以在ForeignKey字段的定义中，通过设置`related_name`来重写`FOO_set`的名字。

反向关联的实现原理是在Django启动时，它会导入所有`INSTALLED_APPS`中的应用和每个应用中的模型模块。每创建一个新的模型时，Django会自动添加反向的关系到所有关联的模型。如果关联的模型还没有导入，Django将保存关联的记录并在关联的模型导入时添加这些关系。由于这个原因，将模型所在的应用都定义在`INSTALLED_APPS`的应用列表中就显得特别重要。否则，反向关联将不能正确工作。

正相关联与反向关联的语法分别如下：

- 正向关联，如c.question，不需要添加`_id`后缀；

- 反向关联默认在类名后加下划线再加‘set’，如q.choice_set指的是q所关联的choice对象集合，用的是Choice这个模型的名字的小写。

~~~python
>>> c = Choice.objects.get(pk=1)
>>> c
<Choice: china>
>>> c.question
<Question: dragon>
>>> q = Question.objects.get(pk=1)
>>> q.choice_set.all()
<QuerySet [<Choice: china>, <Choice: japan>, <Choice: korea>]>
~~~

重写FOO_set`的名字

~~~python
# polls/models.py

class Choice(models.Model):
    # Question与Choice之间是一对多的关系，在“多”的表中设置外键
    objects = models.Manager()  # 默认管理器
    question = models.ForeignKey(
        Question,  # 同一个app中的模型类
        on_delete=models.CASCADE,
        related_name='related_choice')  # 用于反向关联
~~~

反向关联之前需要进行数据库的迁移

~~~python
(py37) G:\NewYear\code\blog\code\mysite>python manage.py makemigrations
(py37) G:\NewYear\code\blog\code\mysite>python manage.py migrate
(py37) G:\NewYear\code\blog\code\mysite>python manage.py shell
>>> q = Question.objects.get(pk=1)
>>> q
<Question: dragon>
>>> q.related_choice.count()
3
~~~

### 模型的元数据 Meta

模型的元数据，指的是“除了字段外的所有内容”，例如排序方式、数据库表名、人类可读的单数或者复数名等等。所有的这些都是非必须的，甚至元数据本身对模型也是非必须的。



### 检索对象 QuerySet

想要从数据库内检索对象，你需要基于模型类，**通过管理器（Manager）构造一个查询结果集（QuerySet）**。

每个QuerySet代表一些数据库对象的集合。它可以包含零个、一个或多个过滤器（filters）。Filters缩小查询结果的范围。在SQL语法中，一个QuerySet相当于一个SELECT语句，而filter则相当于WHERE或者LIMIT一类的子句。其中**pk是主键`primary key`的缩写**。通常情况下，一个模型的主键为“id”。

通过模型的Manager获得QuerySet，每个模型至少具有一个Manager，默认情况下，它被称作objects，可以通过模型类直接调用它，但不能通过模型类的实例调用它，以此**实现“表级别”操作和“记录级别”操作的强制分离**。如下所示：

~~~python
>>> from polls.models import Question
>>> Question.objects
<django.db.models.manager.Manager object at 0x000002A88727A9C8>
>>> q = Question.objects.get(pk=1)
>>> q
<Question: dragon>
>>> q.objects
Traceback (most recent call last):
AttributeError: Manager isn't accessible via Question instances
~~~

从数据库中查找对象时，常用的QuerySet方法使用如下：

- all() ：用于检索所有对象，可以获取某张表的所有记录。
- get()：用于检索单一对象，如果在查询时没有匹配到对象，那么get()方法将抛出DoesNotExist异常，类似地，在使用get()方法查询时，如果结果超过1个，则会抛出MultipleObjectsReturned异常，这两个异常都是模型类的属性。
- filter() ：用于过滤QuerySet的结果，返回一个根据指定参数查询出来的QuerySet。
- exclude()：用于过滤QuerySet的结果，返回除了根据指定参数查询出来结果的QuerySet。

**QuerySets都是懒惰的**

一个创建QuerySets的动作不会立刻导致任何的数据库行为。你可以不断地进行filter动作一整天，Django不会运行任何实际的数据库查询动作，直到QuerySets被提交(evaluated)。简而言之就是，只有碰到某些特定的操作（如print），Django才会将所有的操作体现到数据库内，否则它们只是保存在内存和Django的层面中。这是一种提高数据库查询效率，减少操作次数的优化设计。

每个QuerySet都包含一个缓存，用于减少对数据库的实际操作。对于新创建的QuerySet，它的缓存是空的。当QuerySet第一次被提交后，数据库执行实际的查询操作，Django会把查询的结果保存在QuerySet的缓存内，随后的对于该QuerySet的提交将重用这个缓存的数据。

字段查询

字段查询其实就是filter()、exclude()和get()等方法的关键字参数。 其基本格式是：`field__lookuptype=value`，**注意其中是双下划线**。 例如：

~~~python
>>> from polls.models import Choice
>>> Choice.objects.all()
<QuerySet [<Choice: china>, <Choice: japan>, <Choice: korea>]>
>>> c = Choice.objects.filter(choice_text__startswith='c')  # 字段查询参数
>>> c
<QuerySet [<Choice: china>]>
~~~

其中的字段必须是模型中定义的字段之一。但是有一个例外，那就是ForeignKey字段，你可以为其添加一个“_id”后缀（单下划线）。这种情况下键值是外键模型的主键原生值。例如：

~~~python
>>> Choice.objects.get(question_id=1)
Traceback (most recent call last):
polls.models.Choice.MultipleObjectsReturned: get() returned more than one Choice -- it returned 3!
>>> Choice.objects.all(question_id=1)
Traceback (most recent call last):
TypeError: all() got an unexpected keyword argument 'question_id'
>>> Choice.objects.filter(question_id=1)
<QuerySet [<Choice: china>, <Choice: japan>, <Choice: korea>]>
~~~

关联查询

要跨越某个关联，只需使用关联的模型字段名称，并使用双下划线分隔，直至你想要的字段（可以链式跨越，无限跨度）。

~~~python
>>> Choice.objects.filter(question__question_text='dragon')
<QuerySet [<Choice: china>, <Choice: japan>, <Choice: korea>]>
>>> Choice.objects.filter(question__question_text__contains='dragon')
<QuerySet [<Choice: china>, <Choice: japan>, <Choice: korea>]>
~~~

### 聚合函数

聚合函数用于组合查询。

SQL中聚合函数包括： AVG() ， COUNT() ， MIN() ， MAX() 和 SUM() ，用于计算一组值并返回单个值。

聚合函数不能在django中单独使用，要想在django中使用这些聚合函数，就必须把这些聚合函数放到支持他们的方法内去执行。Django中聚合函数使用之前需要先导入。

Django中支持聚合函数的方法有两种，分别是aggregate和annotate，这两种方法执行的原生SQL以及结果都有很大的区别：

- 第一种方法是使用aggregate()为整个QuerySet生成聚合值，在汇总时不会使用该模型的主键进行group by进行分组，返回结果是字典格式。aggregate的中文意思是聚合, 源于SQL的聚合函数；

```python
>>> from django.db.models import Count
>>> Question.objects.all().aggregate(Count('related_choice'))
{'related_choice__count': 3}
>>> Question.objects.aggregate(Count('related_choice'))
{'related_choice__count': 3}
```

- 第二种方法是使用annotate()为查询集的每个对象生成聚合值（Generating aggregates for each item in a QuerySet），**先分组后聚合**。如查询每个问卷所有的的问题数。返回结果依然是Question QuerySet，只不过多了`related_choice__count`这个字段。如果你不喜欢这个默认名字，你当然可以对这个字段进行自定义从而使它变得更直观。annotate的中文意思是注释，一个更好的理解是分组（Group By）。

~~~python
>>> q = Question.objects.annotate(Count('related_choice'))
>>> q
<QuerySet [<Question: dragon>]>
>>> q[0]
<Question: dragon>
>>> q[0].related_choice__count
3
>>> q = Question.objects.annotate(num_of_choices=Count('related_choice'))
>>> q[0].num_of_choices
3
~~~

## 视图层 Views

视图层是Django处理请求的核心代码层，我们大多数Python代码都集中在这一层面。

它对外接收用户请求，对内调度模型层和模版层，统合数据库和前端，最后根据业务逻辑，将处理好的数据，与前端结合，返回给用户。视图层是真正的后端，是Python工程师的‘主营业务’。

### URL 路由基础

路由的编写方式是Django2.0和1.11最大的区别所在。Django官方迫于压力和同行的影响，不得不将原来的**正则匹配表达式**，改为更加简单的**path表达式**，但依然通过re_path()方法保持对1.x版本的兼容。

路由系统中最重要的path()方法可以接收4个参数，其中2个是必须的：**route和view**，以及2个可选的参数：kwargs和name。其中route 是一个匹配 URL 的准则（类似正则表达式），view指的是处理当前url请求的视图函数。当Django匹配到某个路由条目时，自动将封装的HttpRequest对象作为第一个参数，被“捕获”的参数以关键字参数的形式，传递给该条目指定的视图view。

URL路由在Django项目中的体现就是`urls.py`文件，Django提倡项目有个根`urls.py`，各app下分别有自己的一个`urls.py`（二级路由），既集中又分治，是一种解耦的模式。URL配置(URLconf)就像是 Django 所支撑网站的目录。它的本质是 URL 模式以及要为该 URL 模式调用的视图函数之间的映射表。 

在settings的配置文件中，设置了项目入口顶层的urls的分发器`ROOT_URLCONF`，url匹配是从上往下的短路操作，匹配成功后会给所对应的视图函数传递如下参数：

- 一个HttpRequest 实例。
- 如果匹配的表达式返回了未命名的组，那么匹配的内容将作为位置参数提供给视图。
- 关键字参数由表达式匹配的命名组组成，但是可以被`django.urls.path()`的可选参数kwargs覆盖。

Django在检查URL模式前，会移除每一个申请的URL开头的斜杠(/)。请求的URL被看做是一个普通的Python字符串，URLconf在其上查找并匹配。**进行匹配时将不包括GET或POST请求方式的参数以及域名（如查询字符串）。**

URLconf不检查使用何种HTTP请求方法，所有请求方法POST、GET、HEAD等都将路由到同一个URL的同一个视图。在视图中，才根据具体请求方法的不同，进行不同的处理。

路由转发使用的是include()方法，需要提前导入，它的参数是转发目的地路径的字符串，路径以圆点分割。

每当Django 遇到`include()`时，它会去掉URL中匹配的部分并将剩下的字符串发送给include的URLconf做进一步处理，也就是转发到二级路由去。include的背后是一种即插即用的思想。项目根路由不关心具体app的路由策略，只管往指定的二级路由转发，实现了应用解耦。

demo中根`urls.py`与二级`urls.py`代码分别如下：

~~~python
# mysite/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('control/', admin.site.urls),
]

# mysite/polls/urls.py
from django.urls import path
from . import views

app_name = 'polls'  # 使用URLconf的命名空间区分不同app，分支路由应用名称。多建一层与应用同名的子目录
# 修改模板后需要重启服务，不会自动debug
urlpatterns = [
    # 在路由中给一个路径起了别名，在视图与模板中均可以对别名进行反向解析获得路径的正确地址
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),  # int转换器（path转换器）
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
~~~

### URL 反向解析 

在实际的Django项目中，经常需要获取某条URL，为生成的内容配置URL链接。

比如，我要在页面上展示一列文章列表，每个条目都是个超链接，点击就进入该文章的详细页面。

为避免使用硬编码，Django提供了一种解决方案，只需在URL中提供一个name参数，并赋值一个你自定义的、好记的、直观的字符串。

通过这个name参数，可以反向解析URL、反向URL匹配、反向URL查询或者简单的URL反查。

在需要解析URL的地方，对于不同层级，Django提供了不同的工具用于URL反查：

- 在模板语言中：使用`url`模板标签。(也就是写前端网页时），语法`{% url "别名" %}`；
- 在Python代码中：使用`reverse()`函数。（也就是写视图函数等情况时），语法`reverse("别名")`；
- 在更高层的与处理Django模型实例相关的代码中：使用`get_absolute_url()`方法。(也就是在模型model中)

但是有可能出现重名的冲突，因此引入**URL命名空间**。Django中与命名空间相关有两个概念，[app_name和namespace](https://blog.51cto.com/jiajinh/2432449)，分别用于解决如下问题：

- app_name：在多个app之间，有可能产生同名的url，这个时候避免反转url的时候混淆，可以使用应用命名空间做区分。应用命名空间使用。在应用url中定义 app_name；
- namespace：一个app应用可以有多个实例部署，即创建多个url映射到一个app中，所以就会产生一个问题，在做反转的时候，如果不使用命名空间，就会混淆，为了避免这个问题。我们可以使用实例命名空间。在include函数中添加namespace即可。

存在URL命名空间时，反向解析需要在别名前[添加命名空间](https://blog.csdn.net/ifubing/article/details/100601860)，即`"命名空间:别名"`。







