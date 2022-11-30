from bind_pool_executor.main import BindProcessPoolExecutor
from time import sleep
from random import randint

def do_job(num):
    sleep_sec = randint(1, 10)
    print('value: %d, sleep: %d sec.' % (num, sleep_sec))
    sleep(sleep_sec)


"""
如果你使用标准模块“concurrent.futures”，同时要处理几百万条数据，那么一个worker队列就会占用所有空闲内存。
如果脚本在弱 VPS 上运行，这将导致内存泄漏。
BoundedProcessPoolExecutor VS ProcessPoolExecutor
有界进程池执行器
BoundedProcessPoolExecutor 只会在另一个 worker 完成工作时将新 worker 放入队列。
"""

with BindProcessPoolExecutor(max_workers=5) as worker:
    for num in range(10000):
        print('#%d Worker initialization' % num)
        worker.submit(do_job, num)