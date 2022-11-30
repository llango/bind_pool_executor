# bind-pool-executor


[![PyPI version](https://badge.fury.io/py/bind-pool-executor.svg)](https://badge.fury.io/py/bind-pool-executor)
![versions](https://img.shields.io/pypi/pyversions/bind-pool-executor.svg)
[![GitHub license](https://img.shields.io/github/license/mgancita/bind-pool-executor.svg)](https://github.com/mgancita/bind-pool-executor/blob/main/LICENSE)


[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)


捆绑池处理，在一个工作执行完开始另一个工作的执行

## 安装

```
pip install bind-pool-executor
```

## 操作

进程操作方式：
```python

from bind_pool_executor.main import BindProcessPoolExecutor as Pool
import time 
import random

def do_job(num):
    sleep_sec = random.randint(1, 10)
    print('value: %d, sleep: %d sec.' % (num, sleep_sec))
    time.sleep(sleep_sec)

with Pool(max_workers=5) as worker:
    for num in range(10000):
        print('#%d Worker initialization' % num)
        worker.submit(do_job, num)

```

线程操作方式：
```python

from bind_pool_executor.main import BindProcessPoolExecutor as Pool
import time 
import random

def do_job(num):
    sleep_sec = random.randint(1, 10)
    print('value: %d, sleep: %d sec.' % (num, sleep_sec))
    time.sleep(sleep_sec)

with Pool(max_workers=5) as worker:
    for num in range(10000):
        print('#%d Worker initialization' % num)
        worker.submit(do_job, num)

```

## 许可
开源许可: MIT

## 制作
该包使用 [Cookiecutter](https://github.com/audreyr/cookiecutter) 和 [`llango/cookiecutter-mkdoc-shapackage`](https://github.com/llango/cookiecutter-mkdoc-shapackage/) 项目模版创建。
