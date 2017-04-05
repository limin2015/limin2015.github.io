---
layout:     post
title:      paper-openfoam-optimization-1(中文文献)
keywords:   openfoam-optimization
category:   paper
tags:       [paper]
---

**前言：**

	本文主要整理针对OpenFoam的加速的一些中文论文。看看大体大家都在做什么，哪些点。属于对OpenFoam调研的初级阶段。

## 基于GPU的OpenFoam的优化
**来源**：
这是上交大的一个硕士毕业论文。

## 主要内容：
1.加速icoFoam中的一些函数。

2.针对解法器，在Thrust和CUSP的基础上，开发了一个解法器的小插件。其实就是把解法器那个函数单独拿出来进行了GPU加速。

## 详细内容
1.将openfoam的稀疏矩阵的格式：lduMatrix存储格式转化为csr格式。

2.加速了预条件共轭梯度（CG）和预条件稳定双共轭（PBiCG）。里面的spmv使用自己搞的一个算法实现。其他的dot操作等，直接调用thrust库和cusp库中的函数实现。

3.预条件有很多种：本文只实现了最简单的一种：对角处理。

## 展望
1. GAMG（多重网格）方法，用的很多，但是目前还没有加速。它说，并行加速有一些困难。（调研一下）

2.  本文只对解法器那个函数单独拿出来优化。所以，上层的应用级解法器icoFoam每次迭代，都调用解法器，进行求解。每次调用的时候都会先把输入矩阵copy到设备内存上，这是一种极大的浪费。因为每次迭代的时候，输入矩阵不变化，所以，可以考虑在应用级算法icoFoam级别，进行整体GPU加速，一次copy就可以啦。减少了数据传输。


## 我的收获
1. 性能分析工具：valgrind（利用它的callgrind分析各个函数调用的开销，找出瓶颈）及kcachegrind（可视化）

（1）valgrind的安装：

下载地址（最新版本）：

http://valgrind.org/downloads/current.html#current

按照readme里讲的：


	./configure;  make; make install;
然后./bashrc里面配置一下PATH和LD_LIBRARY_LIB即可。

注意：

默认安装路径在：/usr/local下面。

我把软件安装在了sq电脑上。

（2）使用


	valgrind /-/-tool=callgrind icoFoam
会生成一个callgraph文件。然后用kcachegrind（在ubuntu软件中心直接下载即可）打开此文件，就会看到各个函数运行的所占的时间比例。

2. 查看OpenFoam中的解法器的类：

	https://cpp.openfoam.org/v4/a02457.html
	
	LduMatrix< Type, DType, LUType >::solver Class 
	
3. 自己整完加法器GPU加速函数后，如何集成到openfoam中：作者介绍了一下大概（可以参考），但是我没有真正看懂。需要试一试。(参考paralution库，可以把自己的solver集成到openfoam中)。



