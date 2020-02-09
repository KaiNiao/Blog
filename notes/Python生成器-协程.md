

### 生成器

1. 概念

- Iterable 可迭代对象，必须要实现 __iter__ 魔法函数或 __getitem__ 方法（可以用for循环）。如字符串、列表。迭代是指更新换代（其实也是重复）的过程，每一次的迭代都必须基于上一次的结果（上一次与这一次之间必须是有关系的） ；
- Iterator 迭代器对象，Iterator类继承自Iterable类，此外必须要实现 __next__ 魔法函数。如生成器对象，可以使用iter(list)将列表转化为迭代器。迭代器是用于迭代取值的工具，提供了一种可以不依赖索引取值的方式 。**迭代器运行结束时报StopIteration异常。**for循环时，从可迭代对象中获取迭代器，自动调用 next() 方法，for循环内部对StopIteration异常进行了处理；
- Generator 生成器对象，可以迭代的，但是只可以读取它一次 ，因为它并不把所有的值放在内存中，它是实时地生成数据；
- yield 是一个类似 return 的关键字，只是这个函数返回的是个生成器。

yield不同于return，带yield的函数是一个生成器，而不是一个函数了，这个生成器有一个函数就是next函数，next就相当于“下一步”生成哪个数，这一次的next开始的地方是接着上一次的next停止的地方执行的，所以调用next的时候，生成器并不会从foo函数的开始执行，只是接着上一步停止的地方开始，然后遇到yield后，return出要生成的数，此步就结束。

2. yield

多线程存在占用内存高、死锁等问题。

使用基于生成器的协程实现 生产者-消费者 模型，代码如下所示。其中 producer() 函数的代码可以合并到 main() 函数中，也就是说 producer() 不是生成器函数。

```python
def producer(c):
    c.send(None)  # 如果没有使用 next(c) 显示启动生成器时使用
    # c.send(1)  # TypeError: can't send non-None value to a just-started generator
    n = 0
    while n < 5:  # 有限循环
        n += 1
        # n = 0  # StopIteration
        print('producer {}'.format(n))

        # 生成器的send(value)方法会将value值“发送”给生成器中的方法。value参数变成当前yield表达式的值。
        # send()方法会返回生成器生成的下一个yield值或者StopIteration异常（如果生成器没有生成下一个yield值就退出了）。
        # 当通过调用send()启动生成器时，value值必须为None，因为当前还没有yield表达式可以接收参数。
        r = c.send(n)  # 将n发送给生成器，r用于接收生成器的返回值
        print('consumer return {}'.format(r))


def consumer():
    r = ''
    while True:  # 死循环
        n = yield r
        if not n:
            return
        print('consumer {}'.format(n))
        r = 'OK'


if __name__ == '__main__':
    c = consumer()
    # next(c)
    producer(c)
```

![这里写图片描述](https://img-blog.csdn.net/20160704123959072)

3. yield from

yield from 后面需要加的是可迭代对象，它可以是普通的可迭代对象，也可以是迭代器，甚至是生成器。

yield from 做了很多的异常处理，如 StopIteration。可用于生成器的嵌套。

yield from iterable本质上等于for item in iterable: yield item的缩写版。





### 协程

https://www.cnblogs.com/chenhuabin/p/10087813.html

在Python中， asyncio、tornado和gevent等模块都实现了协程的功能。

python3.x协程应用：

- asynico + yield from（python3.4）
- asynico + await（python3.5）
- gevent

在Python早期的版本中协程也是通过生成器来实现的，也就是基于生成器的协程（Generator-based Coroutines）。

后来为了简化并更好地标识异步IO，从Python 3.5开始引入了新的语法async和await，可以让coroutine的代码更简洁易读。请注意，async和await是针对coroutine的新语法，要使用新的语法，只需要做两步简单的替换：把@asyncio.coroutine替换为async；把yield from替换为await。



概念

async用于定义协程函数，send方法用于执行函数，await可以针对耗时的操作进行挂起，就像生成器里的yield一样，函数让出控制权，实现切换。asyncio.get_event_loop方法用于自动循环执行所有注册的协程函数，隐式执行而不是显示的通过send方法去执行函数，并且可以实现函数的全部执行。

event_loop事件循环：程序开启一个无限的循环，当把一些函数注册到事件循环上时，满足事件发生条件即调用相应的函数。

coroutine协程对象：指一个使用async关键字定义的函数，它的调用不会立即执行函数，而是会返回一个协程对象，协程对象需要注册到事件循环，由事件循环调用。

task任务：一个协程对象就是一个原生可以挂起的函数，任务则是对协程进一步封装，其中包含任务的各种状态。Task 对象是 Future 的子类，它将coroutine和Future联系在一起，将 coroutine 封装成一个 Future 对象。

future：代表将来执行或没有执行的任务的结果，它和task上没有本质的区别。

async/await 关键字：python3.5 用于定义协程的关键字，async定义一个协程，await用于挂起阻塞的异步调用接口，await就类似于阻塞，暂时执行别的协程。await关键字添加了一个新的协程到循环里，而不需要明确地添加协程到这个事件循环里。



协程的四个状态：

协程可以身处四个状态中的一个。当前状态可以使用inspect.getgeneratorstate(…) 函数确定，该函数会返回下述字符串中的一个：

- GEN_CREATED：等待开始执行
- GEN_RUNNING：解释器正在执行
- GEN_SUSPENED：在yield表达式处暂停
- GEN_CLOSED：执行结束



异步优化的应用场景：IO密集型

异步框架：

- 非阻塞 socket：设置为False；
- 回调  callback：是一种允许多个操作并发等待IO操作的方法，满足一定条件时执行。如使用 selector实现；
- 事件循环 event loop：

协程 coroutine 建立在 Future 类上。标准库 asyncio 本质上是基于生成器的语法糖。

协程拥有回调与线程的优点。

使用协程时，可以将所有的代码放在一个函数中，不需要声明并注册整个调用链，可以重复使用局部变量。

基于协程的异步框架：

- Future 类：Future 类代表一些正在等待但尚未完成的事件，它有一个事件发生时将要被执行的回调列表 self.callbacks。当事件发生时执行所有等待该事件的回调；
- 生成器：程序中止；
- Task 类：负责在生成器上调用 next() 方法。

```python
from selectors import DefaultSelector, EVENT_WRITE, EVENT_READ
import socket
import time

selector = DefaultSelector()  # 自动选择
n_jobs = 0

class Future:
    def __init__(self):
        self.callback = None

    def resolve(self):
        self.callback()

    def __await__(self):
        yield self

class Task:
    def __init__(self, coro):
        self.coro = coro
        self.step()  # 预激协程

    def step(self):  # asyncio
        try:
            f = self.coro.send(None)
        except StopIteration:  # 生成器结束异常
            return

        f.callback = self.step

async def get(path):
    global n_jobs
    n_jobs += 1
    s = socket.socket()
    s.setblocking(False)
    try:
        s.connect(('localhost', 5000))
    except BlockingIOError:
        pass

    f = Future()
    selector.register(s.fileno(), EVENT_WRITE, f)
    await f
    selector.unregister(s.fileno())

    s.send(('GET %s HTTP/1.0\r\n\r\n' % path).encode())
    buf = []

    while True:
        f = Future()
        selector.register(s.fileno(), EVENT_READ, f)
        await f
        selector.unregister(s.fileno())
        chunk = s.recv(1000)
        if chunk:
            buf.append(chunk)
        else:
            break

    # Finished.
    print((b''.join(buf)).decode().split('\n')[0])
    n_jobs -= 1

start = time.time()
Task(get('/foo'))  # get返回生成器
Task(get('/bar'))

while n_jobs:
    events = selector.select()
    for key, mask in events:
        future = key.data
        future.resolve()

print('took %.2f seconds' % (time.time() - start))
```

### IO - 同步，异步，阻塞，非阻

https://blog.csdn.net/historyasamirror/article/details/5778378



![img](https://mmbiz.qpic.cn/mmbiz_png/NtO5sialJZGoRJcJhcDvDdtT2AQRI72pEXgJj2tLqX5A0oQ7QGyOWZOKyK3gibLWEjbxNbHEwo1CP8uo7kCMTyYA/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

