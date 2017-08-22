---
layout: post
title:  paper reading-远程监督关系抽取(Distant Supervision for Relation Extraction via Piecewise
Convolutional Neural Networks)
keywords: 远程监督方法进行关系抽取
categories : NLP
tags:
  - paper
---

TODO！！！
对远程监督关系抽取的几篇论文的总结，本文是第二篇:ACL-2015, 作者为自动化所的zeng diaojian。
是对上一篇CNN关系抽取的改进论文。


## introduction

存在的问题：

1.远程监督生成训练标记数据，可能会标注不正确。

2.使用NLP tools人工提取特征，可能会造成误差累积。

根据上面的2点缺点，本文提出了2个解决方法:

1.将远程监督看做一个multi-instance problem：
the training set consists of many bags,
and each contains many instances. The labels of
the bags are known; however, the labels of the instances in the bags are unknown.

2.提出了PCNN来使用CNN自动提取特征：PCNN是在CNN的基础上，使用分段的max-pooling替换原来的单一的max-pooling，
以此来capture structural information between two entities。


## 相关工作

## 方法介绍

This procedure includes four main parts: Vector Representation, Convolution, Piecewise Max Pooling
and Softmax Output. 

1.


## 实验


## 总结与展望



## 学到的知识


## 引用



## 疑问


## 补充



    