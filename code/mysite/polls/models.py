import datetime

from django.db import models
from django.utils import timezone


# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_time = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        # return self.pub_time >= timezone.now() - datetime.timedelta(days=1)
        # 修复bug
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_time <= now
    # 可以通过给方法提供一些属性来改进输出的样式
    was_published_recently.admin_order_field = 'pub_time'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


class Choice(models.Model):
    # Question与Choice之间是一对多的关系，在“多”的表中设置外键
    objects = models.Manager()  # 默认管理器
    question = models.ForeignKey(
        Question,  # 同一个app中的模型类
        on_delete=models.CASCADE,
        related_name='related_choice')  # 用于反向关联
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

    # 想在模型中增加元数据，方法很简单，在模型类中添加一个子类，名字是固定的Meta，
    # 然后在这个Meta类下面增加各种元数据选项或者说设置项
    class Meta:
        ordering = ['choice_text']  # 表示按'choice_text'字段进行升序排列
        # 用于设置模型对象的直观、人类可读的名称。可以用中文，
        # Django默认会使用小写的模型名作为默认值，同时默认使用复数名称，即verbose_name加上‘s’
        verbose_name = 'All choice'


# 通过运行makemigrations命令，Django 会检测你对模型文件的修改，
# 也就是告诉Django你对模型有改动，并且你想把这些改动保存为一个“迁移(migration)”。
# migrations是Django保存模型修改记录的文件，这些文件保存在磁盘上。
# 在例子中，它就是polls/migrations/0001_initial.py，里面保存的都是人类可读并且可编辑的内容，方便随时手动修改。
# 接下来有一个叫做migrate的命令将对数据库执行真正的迁移动作。

# 将创建和实施迁移的动作分成两个命令两步走，保存一个中间过程的保存文件（migrations），
# 原因是如果通过版本控制系统（例如github，svn）提交项目代码，github不和数据库直接打交道，也没法和你本地的数据库通信。
# 如果没有分为两步，那么github无法知道以及记录、同步、实施你所进行过的模型修改动作，
# 而分为两步之后，你只需要将你的migration文件（例如上面的0001）上传到github，就可以知道这些信息

# 外键：反向关联在类名后加下划线再加‘set’，如q.choice_set指的是q所关联的choice对象集合，用的是Choice这个模型的名字的小写。
# 正向关联，如c.question