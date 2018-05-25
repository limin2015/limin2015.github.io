---
layout: post
title:  paper reading-Sweet KNN An Efficient KNN on GPU through Reconciliation between Redundancy Removal and Regularity
keywords: k-means
categories : paper
tags:
  - paper
---

2017, ICDE (CCF-A)，基于三角不等式的knn算法在GPU上的实现。

## 摘要：

加速KNN很重要。但是Prior efforts in improving its speed have followed two directions with conflicting considerations: 
  
  1. One tries to minimize the redundant distance computations but often introduces irregularities into computations （基于三角不等式等方法，减少计算，但是带来了非规则访存，不利用GPU上并行）
  2. The other tries to exploit the regularity in computations to best exert the power of GPU-like massively parallel processors, which often introduces even extra distance computations. （只考虑并行） 

本文研究了 how to effectively combine the strengths of both approaches. It manages to reconcile the polar opposite effects of the two directions through **elastic algorithmic designs**, **adaptive runtime configurations**, and a set of careful **implementation-level optimizations**. The efforts finally lead to a new KNN on GPU named Sweet KNN, **the first high-performance triangular-inequality-based KNN on GPU** that manages to reach **a sweet point between redundancy minimization and regularity preservation** for various datasets.

## introduction

关于KNN的加速研究，大致可以分为两个方向：

1. 第一个方向: focuses on minimizing the amount of distance computations (algorithm level optimizations)

   (1)基于三角不等式，来减少距离计算
  （2）使用KD-tree存储结构，减少距离计算
  （3）近似算法

**评价**：这些方法减少了距离计算总量，可是也带来了一些计算上的irregularities，导致程序的数据并行性没有以前好了。

2. 第二个方向：better leverage underlying computing systems for acceleration（implementation level optimizations）

**评价**：高性能平台（如GPU）typically **feature massive parallelism best suiting regular data-level parallel computations** (i.e., **the processing of all data points follows the same execution path**), this category of efforts **attempt to enhance the regularity in computations**.


关于这两个研究方向的一个示意图，如下所示：

  ![](/images/paper/sweet-knn-motivation.PNG)


3. 基于以上的两个研究角度的矛盾，本文concentrate on **developing an efficient triangular inequality-based KNN on GPU**. 

  （1）**At the algorithm level**, we introduce an **adaptive design**, which, based on the properties of the current data sets, **automatically adjusts the algorithm and parallelism** on the fly to reach a sweet point between regularity preservation and redundancy minimization. 
  
  （2）**At the implementation level**, we explore **optimizations of data layout** and **data placement on memory** and **thread-data remapping** to remove irregularities in the computations.



## 算法描述

**主要思想**

 

**算法改进**


## 最终的算法


## 对比


## 我的收获

