"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('control/', admin.site.urls),
]

# include语法相当于多级路由，它把接收到的url地址去除与此项匹配的部分，将剩下的字符串传递给下一级路由urlconf进行判断。
# include的背后是一种即插即用的思想。项目根路由不关心具体app的路由策略，只管往指定的二级路由转发，实现了应用解耦
# 路由系统中最重要的path()方法可以接收4个参数，其中2个是必须的：route和view，以及2个可选的参数：kwargs和name
# 其中route 是一个匹配 URL 的准则（类似正则表达式）
# view指的是处理当前url请求的视图函数。当Django匹配到某个路由条目时，
# 自动将封装的HttpRequest对象作为第一个参数，被“捕获”的参数以关键字参数的形式，传递给该条目指定的视图view。