---
layout: post
title:  paper reading：Merge Path - Parallel Merging Made Simple
keywords: paper-并行merge排序
categories : [paper]
tags : [负载均衡]
---

### 来源：2014 IPDPS

### 解决的问题

Parallel merging two sorted arrays。解决这个问题，需要从以下几个方面思考：

- balancing the load among compute
cores
- minimizing the extra work brought about by
parallelization
- minimizing inter-thread synchronization
- Efficient use of memory


### 主要创新点

 1. 提出了一种新的并行分割方式，虽然分割结果和计算复杂度和以前的并行算法相同，但是我们的分割方法是不同的，具有启发性的。
 2. 在此基础上，提出了一种synchronization-free, cache-efficient merging算法（memory-efficient version）。

### 方法详述

 1. 抽象出了merge matrix和merge path两个辅助分割的数据结构。具体如下图所示。
 ![merge matrix and merge path](http://img.blog.csdn.net/20170303163626353?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvdTAxMDQ1ODg2Mw==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)
 
 其中，矩阵是这样构建的：若A[i] >= B[j], 则matrix[i][j] = 1  or matrix[i][j] =0;
 其中，路径就是1与0的交界线（线上有一些点组成，pair（x, y）的集合）。
 
2.  在上一步构造出merge path后，每个线程平均分配任务，如，若共有p个线程，则每个线程处理N/P个任务，第i个线程从第j（j=i*（N/P））个元素开始处理，则每个线程的起始pair是这样获得
的：x+y = j。 所以关键问题是如何求得pair(x, y)。采用二分法来进行搜索。从所有对角线元素中，
二分找到1与0的分界线。

 **algo：**
 ![algo](http://img.blog.csdn.net/20170303163641806?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvdTAxMDQ1ODg2Mw==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)
 
 **example：**
 TODO

### 实验平台及主要的实验结果
 1. 它的实验结果是多线程与单线程比的。（起始单线程效果是比串行差很多的，一方面计算对角线与mergepath交点需要开销，另一方面omp开启有开销。）

 2. n个线程，相比单线程，大约能获得n倍的加速比。 
  
![test performance](http://img.blog.csdn.net/20170303164814088?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvdTAxMDQ1ODg2Mw==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

### 实现代码
1. 在github上发现一份代码：[mergePathOMP](https://github.com/ogreen/MergePathOMP)
2. 我需要自己写一份。