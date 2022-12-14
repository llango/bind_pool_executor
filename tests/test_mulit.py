import concurrent.futures
from time import sleep
from random import randint


def do_job(num):
    sleep_sec = randint(1, 3)
    print('value: %d, sleep: %d sec.' % (num, sleep_sec))
    sleep(sleep_sec)


"""
ProcessPoolExecutor 将所有 worker 插入队列，并期望任务在新 worker 被释放时执行，具体取决于 max_workers 的值
"""
with concurrent.futures.ProcessPoolExecutor(max_workers=5) as worker:
    for num in range(100):
        print('#%d Worker initialization' % num)
        worker.submit(do_job, num)
