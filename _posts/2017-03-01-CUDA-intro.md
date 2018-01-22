---
layout:     post
title:      CUDA的简单介绍
keywords:   安装、架构介绍、常用函数库
category:   CUDA
tags:		[CUDA编程]
---

前言：
GPU作为如今主流的异构计算平台，收到越来越多的追捧，尤其是深度学习的发展，更加催生了其应用。作为并行计算领域的一枚，必须要好好学习一番啦。


# 好的学习资料：

（1） NVIDIA官方的faq：（比如，关于线程数如何设置等问题）
	
	[NVIDIA官方的faq链接](https://developer.nvidia.com/cuda-faq)

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

GTX 280：

Tesla:


Fermi:supports concurrent kernel execution，

Kepler:introducing the Hyper-Q feature，

maxwell:

pascal:



Tesla:K40, K80, P4, P40 and so on.

GeForce(GTX Tian):


P40:2016年发布，专为神经网络推理，支持TensorRT。

P100：


Tesla V100：（架构特征）



总结（几种gpu的对比）：

https://www.cnblogs.com/lijingcong/p/4958617.html

http://we.poppur.com/thread-2367589-1-1.html


Fermi   - NVIDIA compute capability 2.x cards
Kepler  - NVIDIA compute capability 3.x cards
Maxwell - NVIDIA compute capability 5.x cards
Pascal  - NVIDIA compute capability 6.x cards
Volta   - NVIDIA compute capability 7.x cards



## 我的127服务器

### 基本信息： 

是Tesla K40m" with compute capability 3.5

CUDA核心数量：2880

双精度浮点性能：1.43 Tflops，单精度浮点性能：4.29 Tflops（3:1）

显存总容量：12GB ； share-memory：

显存带宽: 288GB/s 支持PCI-E 3.0；  传输带宽从8GB/s（tesla k20）近乎翻番至15.75GB/s；

功耗：235W热设计功耗 被动散热

GPUBoost feature：其实就是可以设置clock frequency。

[是什么，如何开启？](http://blog.csdn.net/gold0523/article/details/52675708)


### 服务器上的一些命令：

    qnodes //查看所有的节点信息
    qnodes -q gpu03 //查看节点gpu03的一些信息（包括gpu占用率和显存使用量等）
    qstat           //查看当前作业提交情况

     




# gpu上的一些高性能的函数库：

blas：

thrust：

NPP：

CULA是什么库？开源吗：基于CUDA的一个lapack库。


