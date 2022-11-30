from multiprocessing import Process, Lock, Semaphore
import os
import time


def test(n, lock):
    lock.acquire()
    print('%s: %s 正在运行...' % (n, os.getpid()))
    time.sleep(1)
    print("%s: %s 完成" % (n, os.getpid()))
    lock.release()


if __name__ == "__main__":
    lock = Semaphore(4)
    for i in range(5):
        p = Process(target=test, args=(i, lock))
        p.start()
