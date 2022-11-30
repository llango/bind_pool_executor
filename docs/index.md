# bind-pool-executor

捆绑池处理，在一个工作执行完开始另一个工作的执行

## python并发编程之Semaphore

Semaphore类实现了信号量对象，可用于控制获取资源的线程/进程数量。所具有的acquire()和release()方法，可以用with语句的上下文管理器。当进入时，将调用acquire()方法，当退出时，将调用release()。

```python

def acquire(blocking=True, timeout=None):
    """
        blocking 当阻塞设置为false时调用时，不阻塞，否则阻塞。
        timeout 设置超时秒。如果未在时间间隔内完成，返回false；否则返回true
        return True/False
    """
    pass

def release():
    """
        释放一个信号量，将内部计数器加1。当计数器在进入时为零，而另一个线程正在等待它,若要再次大于零，请唤醒该线程
    """
```

示例:

```python

import threading 
import time 

def hello(n, sema):
    sema.acquire()
    print('调用线程 {0}'.format(n))

# 信号量管理表示realse()调用数减去acquire()调用数加上去一个初始值的计数器　　1　-　5　+　0　＝　-4　
sema = threading.Semaphore(value=0)
workers = 5
for n in range(workers):
    t = threading.Thread(target=hello, args=(n+1, sema, ))
    t.start()
 
time.sleep(3)
print('开启线程')
sema.release()
```

Semaphore信号量相比Lock锁，可以控制进入进程/线程的数量
Lock一次只允许一个进程/线程进入
Semaphore(n)则可以允许n个进程/线程进入

示例:

```python

from multiprocessing import Process, Lock, Semaphore
import os 
import time 

def test(n, lock):
    lock.acquire()
    print('%s: %s 正在运行...' %(n, os.getpid()))
    time.sleep(1)
    print("%s: %s 完成" % (n, os.getpid()))
    lock.release()

if __name__ == "__main__":
    lock = Semaphore(4)
    for i in range(5):
        p = Process(target=test, args=(i, lock))
        p.start()
```