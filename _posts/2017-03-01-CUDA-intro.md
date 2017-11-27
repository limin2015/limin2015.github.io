---
layout:     post
title:      CUDA的简单介绍
keywords:   安装、基本接口、小例子
category:   CUDA
tags:		[CUDA编程]
---

前言：
GPU作为如今主流的异构计算平台，收到越来越多的追捧，尤其是深度学习的发展，更加催生了其应用。作为并行计算领域的一枚，必须要好好学习一番啦。


# 好的学习资料：

（1） NVIDIA官方的faq：（比如，关于线程数如何设置等问题）
	
	https://developer.nvidia.com/cuda-faq

（2）gpu官网上的一些资料（easy-reading）：
[even-easier-introduction-cuda](https://devblogs.nvidia.com/parallelforall/even-easier-introduction-cuda/)

[how-implement-performance-metrics-cuda-cc](https://devblogs.nvidia.com/parallelforall/how-implement-performance-metrics-cuda-cc/)

[how-query-device-properties-and-handle-errors-cuda-cc](https://devblogs.nvidia.com/parallelforall/how-query-device-properties-and-handle-errors-cuda-cc/)

[how-optimize-data-transfers-cuda-cc](https://devblogs.nvidia.com/parallelforall/how-optimize-data-transfers-cuda-cc/)

[how-optimize-data-transfers-cuda-cc](https://devblogs.nvidia.com/parallelforall/how-optimize-data-transfers-cuda-cc/)

[how-overlap-data-transfers-cuda-cc](https://devblogs.nvidia.com/parallelforall/how-overlap-data-transfers-cuda-cc/)

[如何使用好global memory？](https://devblogs.nvidia.com/parallelforall/how-access-global-memory-efficiently-cuda-c-kernels/)

[AXPY:](https://devblogs.nvidia.com/parallelforall/six-ways-saxpy/)



# GPU各种架构、型号整理

G80、 Maxwell 和 Pascal 5 
 



## 架构整理：TODO

Fermi:

Kepler:
maxwell

pascal:

Tesla:

Tesla:K40, K80, P4, P40 and so on.

GeForce(GTX Tian):


P40:2016年发布，专为神经网络推理，支持TensorRT。

P100：


Tesla V100：（架构特征）



## 例子整理（11.27整理）


TODO:

1.下面的结果failed：OK

/home/limin/CUDATrain/svm/lmblas/vectorAdd

2。结果是：CUDA driver version is insufficient for CUDA runtime version: OK

/home/limin/CUDATrain/svm/lmblas/dot

3.下面的axpy调通：thrust和手写的，测试一下性能。

/home/limin/CUDATrain/svm/lmblas

4.pi的那个例子，也出现了error：OK

CUDA driver version is insufficient for CUDA runtime version



5.会调用blas库中的函数：scal和gemv

/home/limin/CUDATrain/svm/lmblas/scal

6.blas的文档：

[blas-document](http://docs.nvidia.com/cuda/cublas/#examples)



