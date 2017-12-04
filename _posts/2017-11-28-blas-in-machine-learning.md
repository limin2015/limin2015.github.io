---
layout: post
title:  blas库在机器学习算法中的应用
keywords: paper
categories : [paper]
tags : [paper]
---

调研一下哪些机器学习算法会调用blas数学库中的函数，如何用的？

# 聚类算法： kmeans

这个我做了：要么使用改进的gemv，要么使用改进的gemm；


# 分类算法： knn

实际上是用到了一个距离矩阵的求解（类GEMM操作）；



# SVM算法

实际上是用到了改进的GEMV函数；GEM2V函数（融合函数）

下面的这篇关于libsvm的代码解析的专栏不错：
http://blog.csdn.net/column/details/libsvm.html


# EM算法（最大期望算法）：查查！！！


# PageRank算法：看看！！


# 其他的：（查一查，看看是如何使用的）

KL变换、条件随机场、随机游走模型（宽平稳）、马尔科夫随机场，贝叶斯；


# 深度学习算法：如CNN、RNN等；

caffe中的卷积使用的是：img2col+gemm;
还有一种卷积计算方法，使用FFT；


总结：（深度学习框架中用到的blas函数有哪些）

卷积层->pool层->sigmoid->relu->softmax->全连接层（or inner_product层）
->batch-normalization->tanh->lstm->lrn->img2col->drop-out

挨个看看，每个是大体如何实现的(caffe为例)：

全连接层：调用的gemv或者gemm，根据参数的值，选择的（需要看看）（forward和backward）

卷积层： img2col + gemm;或者cudnnGetConvolutionForwardAlgorithm（调用cudnn中的算法）


pooling层：


scal：
sum：







