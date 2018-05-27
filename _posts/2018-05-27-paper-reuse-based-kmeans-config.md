---
layout: post
title:  paper reading-Reuse-Centric K-Means Configuration
keywords: k-means
categories : paper
tags:
  - paper
---

2018, ICDE（CCF-A）, 短文，yufen ding组的论文

## introduction

机器学习算法一般都是需要调参的。需要设置不同的参数，多次跑这个算法。我们把每一次的调参，然后跑一次算法的过程，叫做一次配置config。比如k-means算法，通过设置不同的k值，来得到最好的聚类结果。

之前的大部分算法优化都是从参数固定情况下的（一个config内部），来考虑加速算法。本文从算法在多次config下的情况下，进行算法的优化。（这个思路挺好的，有这个需求。）

本文解决的问题是：在多次配置下，多次跑k-means情况下，如何提速？


首先，k-means需要配置的参数：

  k值的选取；
  特征的维度选择多大：（我之前没想到的）因为本文的输入数据集的特征是采用PCA处理后的特征，故可以设置特征维度。

其次，在下一节算法描述中介绍作者的3个优化方法：reuse-based filter，center reuse，Two-Phase Design.


## 算法描述

**解决问题的出发点**：多次调用的时候，k取值不同的时候，基于三角不等式的k-means还能有所改进吗？

普通的算法：每次迭代都需要计算所有样本点到所有中心点的距离；
基于三角不等式减少距离计算的算法：Modern k-means algorithms (e.g., Yingyang k- means [3]) successfully avoid many distance calculations in later iterations of a k-means, but they all still need the n×k distance calculations in the first iteration of k-means. In our experiments, we observe that the first iteration weights up to 40% of the entire k-means time. We call it **the first iteration problem**（这个结论非常的好！！）. 每次配置的时候第一次迭代都需要计算所有样本点到所有中心点的距离。故，我们想到利用三角不等式及上一次config的结果，优化下一次config的第一次迭代的计算。


**具体内容**：

1. reuse-based filter（基于重用的过滤法）

Reuse across k：

当下一次config和上一次config的特征集相同，k的值不同时：使用三角不等式来减少下一次config的第一次迭代的距离计算数目（它的这个前提是下一次config的初始化中心点的设置采用了上一次config的最终中心点这一结果）。

   ![](/images/paper/reuse-kmeans-1.PNG)


Reuse across feature sets：

当下一次的config的特征集是上一次的config的子集，且两次config的k值相同时：它的方法没大看懂！！


2. center reuse

思想：下一次config的初始化的中心点设置为上一次config的最终结果中产生的中心点。

（1）Reuse across validations：

在不同folds的交叉验证时使用。

（2）Reuse across k：

  Suppose that the reuse is from one configuration with k = k1 to another with k = k2. If k2 > k1, in addition to using the centers
  attained in exploring the earlier configuration, we add k2−k1 randomly generated centers as needed. If k2 < k1, we cluster the k1 centers into k2 groups and then take the group centers as the initial centers for the exploration of the latter configuration.

（3）Reuse across feature sets：没看懂！！


3. Two-Phase Design：没看懂！！


## 我的收获

1. 本文的整个内容我认为有很多地方是有问题的，很多没有解释清楚，很多没有看懂。

2. 可以借鉴的地方就是：reuse-based filter方法中的Reuse across k部分，这个**利用三角不等式来消除第一次迭代中的距离计算的数目**的想法还可以。
