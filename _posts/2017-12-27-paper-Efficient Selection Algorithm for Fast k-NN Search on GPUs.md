---
layout:     post
title:      paper-Efficient Selection Algorithm for Fast k-NN Search on GPUs
keywords:   knn optimization（array-top-k）
category:   [paper]
tags:       [paper]
---

# 出处：

2015, IPDPS, 上海交大的一个博士的成果， 有源码

[source-code](https://sites.google.com/site/xxtang1988/projects）


# 要解决的问题：

knn中的array-top-k的在GPU上的并行。

**本质上**：
对top-k来说，其实就是维持一个含有k个元素的数组，然后对于后面的元素挨个的符合条件（小于数组中的最大值）的插入到这个数组中。可以采用的数组的数据结构是：insert-queue，heap-queue, merge-queue.
本文实际上，是对这3个数据结构的算法的top-k实现在gpu上，然后发现效果不好，先提出了一个merge-queue的数据结构；
然后从branch divergence（buffer的方法），减少插入次数（hierarchy partition）这几个层面对之前的3个数据结构的进行了优化。

# merge-queue

为啥要提出merge-queue，他有啥好处吗？


# 学习本文的方法

buffer：
感觉buffer这个技术用的不错！！

hierarchy partition：
这个方法跟DC-TOP-K(2016-icpp)有啥区别和联系呢？？



# 阅读源码：

fgknn的源码（GPU）非常好，非常清晰。提供了一个距离矩阵计算的函数和array-topk的诸多函数（方便后面修改调用）。

array-insert-sort：

array-heap-sort:

array-bitonic-sort:  
http://blog.csdn.net/jiange_zh/article/details/49533477



# 知识补充：

1. bitonic sort（并行算法）：

[并行计算-Bitonic Sort（双调排序）基础](http://blog.csdn.net/jiange_zh/article/details/49533477)

http://blog.csdn.net/xbinworld/article/details/76408595

[这篇论文讲gpu上的集中排序的实现](http://blog.csdn.net/abcjennifer/article/details/47110991)


2. 