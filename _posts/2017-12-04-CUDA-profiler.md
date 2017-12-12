---
layout: post
title:  CUDA性能优化-调优工具
keywords: CUDA
categories : [CUDA]
tags : [CUDA编程]
---

调优工具的使用。。。。。。


# 调优工具相关：



## nvidia 官方文档：

[链接](http://docs.nvidia.com/cuda/profiler-users-guide/index.html#axzz30ouNvjWo)


## device上可以printf吗？

Specifically, for devices with compute capability less than 2.0, the function cuPrintf is called;     otherwise, printf can be used directly.

高于2.0的机器，编译的时候加上： -arch=sm_20， 直接调用printf（用法同普通的c程序）就可以实现。






##  nvprof和nvvp（可产生sass代码）


PTX:

https://book.2cto.com/201409/46640.html



## ptxas是什么？

nvcc -Xptxas –v acos.cu 

ptxas info : Compiling entry function 'acos_main' 

ptxas info : Used 4 registers, 60+56 bytes lmem, 44+40 bytes smem, 20 bytes cmem[1], 12 bytes cmem[14] 

这里对上例进行一个简单的解释，smem表示共享存储器，这个地方它被分成了两个部分，第一个表示总共声明的共享存储器大小，后者表示系统在存储段中分配的数据总量：共享存储器中的device函数参数块和局部存储器中的线程索引信息。cmem表示常量存储器的使用情况，这里就是使用了一个20bytes的变量和一个长度为14的单位12byte的数组.
上面是从网上看到一个结果和对结果的的解释，感觉不太对，我计算过了smem加号前面的大小等于声明的sharememory的大小加上核函数参数数量乘以每个变量的字节数，后面的就不清楚是怎么算出来的了，后面对cmem的解释可能是错误的，我定义了__device__ __constant__ int cu_voiinf[6];        __device__ __constant__ int cu_phainf[6];但显示的是 72 bytes cmem[0], 148 bytes cmem[1]，所以对cmem可能不正确。








