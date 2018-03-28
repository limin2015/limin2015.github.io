---
layout: post
title:  CUDA性能优化-pinned memory
keywords: CUDA
categories : [CUDA]
tags : [CUDA编程]
---



## 页锁定内存和可分页内存的对比

1.
CUDA use DMA to transfer pinned memory to GPU. Pageable host memory cannot be used with **DMA** because they may reside on the disk. If the memory is not pinned (i.e. page-locked), it's first copied to a page-locked "staging" buffer and then copied to GPU through DMA. So using the pinned memory you save the time to copy from pageable host memory to page-locked host memory

**ref**：
<https://stackoverflow.com/questions/5736968/why-is-cuda-pinned-memory-so-fast>



pinned memory分配的空间位于物理内存，即RAM中，故可分配的最大pinned memory肯定要小于RAM的大小，具体可以多少呢？
参考下面这个问题：

**ref**：
<https://stackoverflow.com/questions/12439807/pinned-memory-in-cuda>




2.
下面这个blog实验不错：（测试cpy时间：）

**ref**：
<http://blog.csdn.net/dcrmg/article/details/54975432>



## Using async memcopy without using cudaMallocHost/cudaHostAlloc? 

这个问题问的不错：

**ref**：
<https://devtalk.nvidia.com/default/topic/463301/cuda-programming-and-performance/using-async-memcopy-without-using-cudamallochost-cudahostalloc-/>



