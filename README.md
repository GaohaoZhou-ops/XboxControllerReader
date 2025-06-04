# XBox Controller Reader

## English
This repository uses Python to perform IO on each button of the XBox game controller, and provides two encapsulation classes, asynchronous and synchronous, as well as corresponding test scripts.

It is recommended to use it together with my blog: [《AirSim/Cosys-AirSim 游戏开发（一）XBox 手柄 Windows + python 连接与读取》](https://blog.csdn.net/nenchoumi3119/article/details/148424720?spm=1001.2014.3001.5501#t5)

----

### File Description

* `main.py`: provides asynchronous and synchronous IO tests;
* `simplest_test.py`: the most basic synchronous test;
* `xbox_controller_async.py`: asynchronous IO class encapsulation;
* `xbox_controller_sync.py`: synchronous IO class encapsulation;

### How to Use

Before running the code, you need to install the following dependencies:
```bash
$ pip install pygame
```

Run the following script to test whether the controller is connected correctly:
```bash
$ python simplest_test.py
```

Run the following script to test whether asynchronous and synchronous IO are normal:
```bash
$ python main.py
```

### Update Logs

* 2025-06-04：Encapsulates asynchronous and synchronous classes.

----

## Chinese 

这个仓库通过 pyhton 对用 XBox 游戏手柄进行各个按键的 IO，提供了异步与同步两个封装类，以及对应的测试脚本。

建议配合我的博客一起使用：[《AirSim/Cosys-AirSim 游戏开发（一）XBox 手柄 Windows + python 连接与读取》](https://blog.csdn.net/nenchoumi3119/article/details/148424720?spm=1001.2014.3001.5501#t5)

### 文件描述

* `main.py`：提供了异步与同步IO测试；
* `simplest_test.py`：最基础的同步测试；
* `xbox_controller_async.py`：异步IO类封装；
* `xbox_controller_sync.py`：同步IO类封装；

### 如何使用

在运行代码之前需要安装下面的依赖：
```bash
$ pip install pygame
```

运行下面的脚本测试手柄是否正确连接：
```bash
$ python simplest_test.py
```

运行下面的脚本测试异步与同步IO是否正常：
```bash
$ python main.py
```

### 更新日志
* 2025-06-04: 封装了异步与同步类