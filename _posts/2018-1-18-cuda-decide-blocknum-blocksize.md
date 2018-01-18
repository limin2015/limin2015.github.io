---
layout: post
title:  CUDA性能优化-如何确定块数，和块内线程数
keywords: CUDA
categories : [CUDA]
tags : [CUDA编程]
---

TODO: 我还是不大明白！！


## 确定每一块中的线程数，和每个grid中的块数的原则是什么？（太重要了的！！）

1. active-thread和active-block是如何计算出来的？

这是通过设备属性查询出来的值：

  Total amount of constant memory:               65536 bytes
  Total amount of shared memory per block:       49152 bytes
  Total number of registers available per block: 65536
  Warp size:                                     32
  Maximum number of threads per multiprocessor:  2048
  Maximum number of threads per block:           1024


2. 

（1）too much shared memory allocated to one block limits the number of active blocks per multiprocessor:
若一个块内分配的shmem太多，则活跃的块数就会受限制。（有什么具体的关系吗？）



（2）

## 寄存器使用过多成为CUDA程序瓶颈的情况分析：（还没看）

http://blog.csdn.net/u013443737/article/details/23422569

3.  nvidia的sample的SDK中有一个计算工具：
    NVIDIA_CUDA-8.0_Samples/0_Simple/simpleOccupancy

4.

