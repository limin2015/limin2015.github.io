---
layout:     post
title:      softmax与sigmoid函数
keywords:   softmax， sigmoid
category:   [machine-learning]
tags:       [machine-learning-basic]
---

Softmax，sigmoid在机器学习中有非常广泛的应用，本文主要是总结一下它们的特点及如何应用。（原理搞明白！）

## Softmax介绍




### 定义：

softmax  is a generalization of the logistic function that "squashes" a K-dimensional vector {\displaystyle \mathbf {z} } \mathbf {z}  of arbitrary real values to a K-dimensional vector {\displaystyle \sigma (\mathbf {z} )} \sigma (\mathbf {z} ) of real values in the range [0, 1] that add up to 1. 

[](/images/machine-learning/softmax-1.png)


###大家的理解：

1.如果某一个zj大过其他z,那这个映射的分量就逼近于1,其他就逼近于0，主要应用就是多分类，sigmoid函数只能分两类，而softmax能分多类，softmax是sigmoid的扩展。

2.为什么要取指数，第一个原因是要模拟max的行为，所以要让大的更大。第二个原因是需要一个可导的函数.

3.把一堆实数的值映射到0-1区间，并且使他们的和为1.

4.

## sigmoid介绍




## 总结：




## 参考文献：
1. https://www.zhihu.com/question/23765351(知乎)

2.

