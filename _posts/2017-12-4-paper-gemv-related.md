---
layout:     post
title:      paper-GEMV-related
keywords:   paper
category:   [paper]
tags:       [paper]
---

本篇博客整理了GEMV（稠密矩阵乘向量）相关函数在GPU上的优化的paper。学习他们的优化方法。


# 第一篇：Fast Implementation of General Matrix-Vector Multiplication (GEMV) on Kepler GPUs

## 出处：
2015-Euromicro International Conference on Parallel, Distributed, and Network-Based Processing（ccf列表中没有）

## 摘要：

在Kepler架构上，实现了一个列优先的GEMV函数。在原来的typical blocking techniques for shared-memory and
register along with 128-bit vector load/store instructions优化方法的基础上，本文发现随着问题规模的变化，性能会有波动。针对这一现象，本文发现它跟块大小有关，设计了一个设置最优块大小的方法（基于性能模型分析的，不是跑多组实验然后决定的）。不仅可以在kepler架构上跑的好，在maxwell架构上也可以。


## 前人工作

基本的优化方法：

1.分块方法：一个grid里有一个块，一个块里有Tx*Ty个线程。
2.share-memory的使用：使用share-memory来存储x；
3.128位的load/store instructions来读取矩阵和x（如何实现呢？）；


## 本文主要内容：

重点是：如何决定的块大小。寄存器到底多少，如何掩盖访存开销？



### the proposed algo：


## 我的疑问
1. 128bit load/store instructions（vector load/store）是如何实现的？
向量化呗！！可是simd指令对于gpu适用吗？

2.


## 我的收获



