---
layout: post
title:  CUDA性能优化-bank-confilict
keywords: CUDA
categories : [CUDA]
tags : [CUDA编程]
---

# 存储体冲突是什么？

bank-conflict:


#如何减少存储体冲突？


## 关于bank conflict的解释：

![](/images/cuda/bank-conflict.png)

一个块内的线程，最好相邻线程访问的是相邻的内存。否则容易bank conflict。


下面的介绍很好：（good！！）

http://blog.csdn.net/u013701860/article/details/50253343



