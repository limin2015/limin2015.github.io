---
layout:     post
title:      paper-SM-Centric Scheduing on GPU
keywords:   paper-VersaPipe-2017
category:   [paper]
tags:       [paper]
---



本文是对于以下2篇文章的总结：（第一篇文章的写作太好了，学习！！）

**SM-Centric Transformation, Circumventing Hardware Restrictions for Flexible GPU Scheduling**

**Enabling and Exploiting Flexible Task Assignment on GPU through SM-Centric Program Transformations**



# 出处：

BoWu 的 PACT’14的短文，和ICS’15的长文


# 摘要


# persistent thread存在的问题

1. The first limitation comes from the randomness in the hard- ware scheduler. Our experiments showed that the schedul- ing is not round-robin, contrary to common perception, and does not guarantee an even distribution of thread blocks, even if the number of thread blocks is small. Hence, persistent threads may underutilize hardware resource if some SMs obtain less thread blocks than others.

2. persistent threads has no support for deciding on which SM a task should run, which is important for some optimizations of locality enhancement.


本文解决了persistent thread存在的2个问题，主要用到的方法是：SM-centric task selection and a filling-retreating scheme


