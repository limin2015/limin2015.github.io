---
layout: post
title:  CUDA性能优化-调优工具
keywords: CUDA
categories : [CUDA]
tags : [CUDA编程]
---

调优工具的使用。。。。。。


#调优工具相关：



## nvidia 官方文档：

http://docs.nvidia.com/cuda/profiler-users-guide/index.html#axzz30ouNvjWo


## device上可以printf吗？

Specifically, for devices with compute capability less than 2.0, the function cuPrintf is called;     otherwise, printf can be used directly.

高于2.0的机器，编译的时候加上： -arch=sm_20， 直接调用printf（用法同普通的c程序）就可以实现。



## #if (__CUDA_ARCH__ >= 200)这句是什么意思：



##  nvprof和nvvp（可产生sass代码）


PTX:

https://book.2cto.com/201409/46640.html








