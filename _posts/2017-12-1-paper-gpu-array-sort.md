---
layout:     post
title:      paper-GPU-ArraySort: A parallel, in-place algo for sorting large number of arrays
keywords:   GPU-ArraySort
category:   [paper]
tags:       [paper]
---

## 出处：
2017年，ICPP

## 要解决的问题：

1. 之前的并行排序，只关注一个数组（元素比较多）的元素的排序；从来没有人研究过多个数组的排序的并行算法。

## 摘要：

1.做了一个多个数组排序的GPU上的并行算法。（实际上是使用的sample-sort的算法）
2.与普通的方法进行比较性能（速度和内存使用量）：普通方法使用的是调用thrust算法中的基于k的排序（调用好几次），这个普通方法想法也挺好的。


## 前人工作

1.GPU上的并行排序有哪些算法：需要稍微整理一下，大概知道算法是如何并行的：

m-way-merge-sort、bucket sort、sample-sort、radix sort、quick-sort、odd-even sort


2. sample-sort的算法：以下文章总结的非常好：

[sample-sort](http://www.jianshu.com/p/e8e3b69bc51b)

## 主要内容：

### the proposed algo：

本文的思路：
每一个块处理一个数组。然后每个块内部进行一个多线程的排序。本文选择的算法是sample-sort算法。



### method based on Thrust:


## 补充知识：



## 我的收获

1.新问题的提出，只要能够解决，发好的文章很容易。（要做好调研，做好整理，涉猎广）





