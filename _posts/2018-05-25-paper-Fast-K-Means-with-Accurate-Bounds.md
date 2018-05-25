---
layout: post
title:  paper reading-Fast K-Means with Accurate Bounds
keywords: k-means
categories : paper
tags:
  - paper
---

2016, JMLR (CCF-A). 这篇文章是紧跟yinyang-kmeans之后的一篇文章。

## introduction

已有的几个工作：

  (Elkan, 2003)， (Hamerly, 2010)， Drake (2013)和 Ding (2015)

本文的贡献：

  1. a new bounding-based accelerated exact k-means algorithm, the Exponion algorithm. Its closest relative is the Annular algorithm (Drake, 2013), which is the current state-of-the-art accelerated exact k-means algorithm in low-dimensions. We show that the Exponion algorithm is significantly faster than the Annular algorithm on a majority of **low-dimensional** datasets. （改进了低维度下的一个表现比较好的方法（Drake的方法））

  2. a technique for making bounds tighter, allowing further redundant distance calculations to be eliminated. The technique, illustrated in Figure 1, can be applied to all existing bounding-based k- means algorithms. （提出了一个更紧致的bound，对所有的基于三角不等式的方法都有用。）

  3. 提供了开源的所有的三角不等式的算法的并行实现：
  
    [eakmeans](https://github.com/idiap/eakmeans)


TODO：...



## 摘要：




## 算法描述

**主要思想**

 

**算法改进**


## 最终的算法


## 对比



## 我的收获

