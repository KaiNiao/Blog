from django.urls import path

from . import views


app_name = 'polls'  # 使用URLconf的命名空间区分不同app，分支路由应用名称。多建一层与应用同名的子目录
# 修改模板后需要重启服务，不会自动debug
urlpatterns = [
    # 在路由中给一个路径起了别名，在视图与模板中均可以对别名进行反向解析获得路径的正确地址
    # https://blog.csdn.net/ifubing/article/details/100601860
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),  # int转换器（path转换器）
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]