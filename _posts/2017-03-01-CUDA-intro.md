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

Tesla:

Tesla:K40, K80, P4, P40 and so on.

P40:2016年发布，专为神经网络推理，支持TensorRT。

P100：

最新的V100：（架构特征）

