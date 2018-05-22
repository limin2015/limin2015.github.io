---
layout: post
title:  paper reading-A work efficient parallel sparse matrix sparse vector multiplication algorithm
keywords: SpMSpV
categories : paper
tags:
  - paper
---

发表于2017年的IPDPS：A work efficient parallel sparse matrix sparse vector
multiplication algorithm

## 摘要
1.在多核和KNL上设计了一个多线程的系数矩阵乘系数向量（SpMSpV）的kernel，使用的是openmp。

2.第二节中介绍了优化SpMSpV的关键点：

这个分析很棒，学习！

![](/images/paper/spmspv-keypoints.PNG)


## 算法描述


![](/images/paper/spmspv.png)


## 我的收获

这个paper对于不同的并行方案的取舍的分析很好，有理有据。它提出的并行算法，很好。给人一种看完后恍然大悟，自己却没想到的感觉。并行的过程其实是将串行程序变复杂的一个过程，所以思考起来比较困难。




    