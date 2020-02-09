from django.contrib import admin
from .models import Question, Choice


# Register your models here.
# 在admin站点中注册了Question模型。Django会自动生成一个该模型的默认表单页面
# admin.site.register(Question)
# Django在admin站点中，自动地将所有的外键关系展示为一个select框，添加choice时可以看到
admin.site.register(Choice)


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


# 创建一个继承admin.ModelAdmin的模型管理类，可以自定义模型选项
class QuestionAdmin(admin.ModelAdmin):
    # fields = ['pub_time', 'question_text']
    # 当表单含有大量字段的时候，可以将表单划分为一些字段的集合
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_time'], 'classes': ['collapse']}),
    ]
    # Choice对象将在Question管理页面进行编辑，默认情况，请提供3个Choice对象的编辑区域。
    inlines = [ChoiceInline]
    # 通常，Django只显示__str()__方法指定的内容。可以使用list_display属性，它是一个由字段组成的元组，显示多个字段
    list_display = ('question_text', 'pub_time', 'was_published_recently')  # 属性与方法都可以作为字段被添加
    # 可以对显示结果进行过滤
    list_filter = ['pub_time']
    # 可以添加一些搜索的能力
    search_fields = ['question_text']


admin.site.register(Question, QuestionAdmin)  # 第一个参数则是Question模型本身