---
layout: post
title:  caffe，TensorFlow中的卷积是如何实现的？
keywords: caffe
categories : [deep-learning]
tags : [deep-learning]
---

## caffe中的卷积

1. 以下这个博客讲的非常好：


	http://blog.csdn.net/xiaoyezi_1834/article/details/50786363

两步：

	（1）使用img2col函数，将输入图像和滤波器都展开成矩阵形式。
	（2）调用GEMM进行计算。

## 如何带偏置项的话，咋处理结果？
一个核，加一个偏置


2.贾阳清的解释：（耗内存，但是计算很快；）

	https://github.com/Yangqing/caffe/wiki/Convolution-in-Caffe:-a-memo


## TensorFlow中的卷积（TODO)

mkl数学库， elgen数学库， 










