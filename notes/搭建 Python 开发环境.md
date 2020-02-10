# 搭建 Python 开发环境

## Windows

### 系统

win10。

### 安装 Python3.7

分别需要安装 Python + Pycharm + Anaconda。具体安装网上都有现成教程。

- Python

参考教程[Pycharm及python安装详细教程](https://blog.csdn.net/qq_29883591/article/details/52664478)。

- Pycharm

参考猪哥教程[Pycharm的永久激活](https://shimo.im/docs/DJ3h3tJv98ppTYyH/read)。一句话，激活码不好使，需要使用激活补丁，并修改`vmoptions`文件。

![1581245552590](C:\Users\KZ\AppData\Roaming\Typora\typora-user-images\1581245552590.png)

- Anaconda

参考教程[Anaconda的安装及虚拟环境的管理](https://blog.csdn.net/ITLearnHall/article/details/81708148#commentBox)。

[在PyCharm中使用Anaconda创建的环境](https://www.cnblogs.com/anliven/p/9998662.html)，更改Pycharm的解释器选项，注意最终要选择`python.exe`文件。

![1581247235554](C:\Users\KZ\AppData\Roaming\Typora\typora-user-images\1581247235554.png)

### 数据库



## Linux

### 系统

VMware12 + CentOS6.5 + Xshell5

CentOS安装时可能报错，报错信息为：vmware安装ubuntu " [Intel VT-x 处于禁用状态](https://jingyan.baidu.com/article/fc07f98976710e12ffe519de.html)"。

安装完成以后进行如下设置，这样可以避免使用期间不必要的麻烦。

- 设置使系统自动锁屏的时间

System=> preference=>Screensaver=>把时间延长

或者取消勾选 lock screen when screensaver is active 。

- 切换至管理员权限：`su`命令。

- CentOS 6.5关闭防火墙

关闭防火墙：service iptables stop 

永久关闭防火墙：chkconfig iptables off

查看防火墙状态：service iptables status

~~~shell
[kz@localhost ~]$ su
Password: 
[root@localhost kz]# service iptables status
Table: filter
[root@localhost kz]# service iptables stop
iptables: Setting chains to policy ACCEPT: filter          [  OK  ]
iptables: Flushing firewall rules:                         [  OK  ]
iptables: Unloading modules:                               [  OK  ]
[root@localhost kz]# service iptables status
iptables: Firewall is not running.
~~~

分别查看IP地址与系统版本。其中IP地址可用于Xshell连接虚拟机。

~~~shell
[kz@localhost ~]$ ifconfig
eth0      Link encap:Ethernet  HWaddr 00:0C:29:84:B9:78  
          inet addr:192.168.17.128  Bcast:192.168.17.255  Mask:255.255.255.0

lo        Link encap:Local Loopback  
          inet addr:127.0.0.1  Mask:255.0.0.0
[kz@localhost ~]$ cat /etc/issue
CentOS release 6.5 (Final)
Kernel \r on an \m
~~~

查看系统自带的python版本。

~~~shell
[kz@localhost ~]$ python -V
Python 2.6.6
~~~

### 安装 Python3.6

参考教程[Linux下安装Python3.6](https://www.cnblogs.com/kimyeee/p/7250560.html)。

不要动现有的python2环境，实现python3与python2共存。

注意安装完成以后需要创建软链接，否则出现报错信息`command not found`。

~~~bash
[root@localhost Python-3.6.1]# python
Python 2.6.6 (r266:84292, Nov 22 2013, 12:16:22)
[root@localhost Python-3.6.1]# python3
bash: python3: command not found
[root@localhost Python-3.6.1]# ln -s /usr/local/python3/bin/python3 /usr/bin/python3
[root@localhost Python-3.6.1]# python3
Python 3.6.1 (default, Feb  9 2020, 10:42:36) 
[GCC 4.4.7 20120313 (Red Hat 4.4.7-4)] on linux
~~~

安装python3时默认安装pip与setuptools，但pip版本较低，需要进行更新。更新时可能出现报错信息`Network is unreachable`，参考教程[修改pip源](https://blog.csdn.net/sakus/article/details/81003512)至国内镜像。

~~~bash
[root@localhost Python-3.6.1]# pip3 list
Package    Version
---------- -------
pip (9.0.1)
setuptools (28.8.0)
[root@localhost Python-3.6.1]# mkdir ~/.pip
[root@localhost Python-3.6.1]# vi ~/.pip/pip.conf
[root@localhost Python-3.6.1]# pip3 install --upgrade pip
[root@localhost Python-3.6.1]# pip3 list
Package    Version
---------- -------
pip        20.0.2 
setuptools 28.8.0
~~~

### Linux 常用命令

- 文件夹图标右下角有锁，解锁命令

sudo chown -R $USER 文件夹路径，如chown -R $USER code

- vi查找替换命令详解：https://blog.csdn.net/lanxinju/article/details/5731843
- 查看硬盘使用情况：df -h
- vi查找命令：

linux系统里的vi是编辑文本的命令，在vi里查找相应关键字的方法为：

/关键字 ，回车即可。此为从文档当前位置向下查找关键字，按n键查找关键字下一个位置；

？关键字，回车即可。此为从文档挡圈位置向上查找关键字，按n键向上查找关键字。



### 数据库



## 开发前设置

工作中本地Linu通常不需要安装，直接使用Xshell连接公司测试服务器用于开发。

### 跳板机



### Pycharm连接远程服务器

Pycharm连接远程服务器并实现远程调试： 

https://blog.csdn.net/lin_danny/article/details/82185023 

