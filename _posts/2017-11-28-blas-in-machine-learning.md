---
layout: post
title:  blas库在机器学习算法中的应用
keywords: paper
categories : [paper]
tags : [paper]
---

调研一下哪些机器学习算法会调用blas数学库中的函数，如何用的？

分析，总结一下深度学习（cnn和rnn）中的operator的计算模式：

调研一下机器学习的库都有哪些：



# 已有的机器学习库调研：

scikit-learn: python的库。使用方便，但是性能一般。

mlpack：c++的库，支持多线程（如何多线程的？）


benchmark： a modest consumer-grade workstation containing an AMD Phenom II X6 1100T processor clocked at 3.3 GHz and 8 GB of RAM.

	knn（k=3）性能如下图：

	！[](/images/paper/ml-servey-mlpack-knn.png)

	kmeans性能如下图：
	 ！[](/images/paper/ml-servey-mlpack-kmeans.png

	 	

opencv：c++的库，支持多线程（**），支持gpu（**）。主要用于图像处理相关算法，但包含机器学习的一些算法。

matlab：我没用过，需要看一番！！

Shogun：

	http://www.shogun-toolbox.org/



# 机器学习算法的实现方法调研


## 聚类算法： kmeans

这个我做了：要么使用改进的gemv，要么使用改进的gemm；


## 分类算法： knn

实际上是用到了一个距离矩阵的求解（类GEMM操作）；



## SVM算法

实际上是用到了改进的GEMV函数；GEM2V函数（融合函数）

下面的这篇关于libsvm的代码解析的专栏不错：
http://blog.csdn.net/column/details/libsvm.html


## EM算法（最大期望算法）：查查！！！


## PageRank算法：看看！！

注：cuda8.0中的sample中有一个例子。（还有一个sssp（单源最短路径的）的例子）。



## 其他的：（查一查，看看是如何使用的）

KL变换、条件随机场、随机游走模型（宽平稳）、马尔科夫随机场，贝叶斯；


## 深度学习算法：如CNN、RNN等；

caffe中的卷积使用的是：img2col+gemm;
还有一种卷积计算方法，使用FFT(winograd)（nnpack中）；
还有一种：direct compute(mkl-dnn中或者ncnn中);



# why-gemm-is-at-the-heart-of-deep-learning


[why-gemm-is-at-the-heart-of-deep-learning](https://petewarden.com/2015/04/20/why-gemm-is-at-the-heart-of-deep-learning/)



# 总结：（分析深度学习框架中的operator的计算模式）

卷积层->pool层->sigmoid->relu->softmax->全连接层（or inner_product层）
->batch-normalization->tanh->lstm->lrn->img2col->drop-out

挨个看看，每个是大体如何实现的(caffe为例)：

**全连接层**：调用的gemv或者gemm，根据参数的值，选择的（需要看看）（forward和backward）

**卷积层**： img2col + gemm;或者cudnnGetConvolutionForwardAlgorithm（调用cudnn中的算法）

**lstm**: gemm and element-wise operators（to be more detailed!!） 


**pooling层**：


**sigmoid**:

**relu**: max(0, x);

**tanh**:

**softmax**:


**scal**：

**sum**：







