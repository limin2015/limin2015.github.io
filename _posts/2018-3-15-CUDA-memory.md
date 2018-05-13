---
layout: post
title:  CUDA性能优化-memory相关的
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



# 异步传输相关

## cudaMemcpyAsync：异步传输

注意用于异步传输的数组，必须是in page locked（又叫pinned memory） memory（内存空间是物理地址，没有对应的虚拟地址。）



## cudaMemcpyToSymbol有没有对应的异步的函数

有。

在下面的页面可以搜到：cudaMemcpyToSymbolAsync //Copies data to the given symbol on the device

    http://docs.nvidia.com/cuda/cuda-runtime-api/group__CUDART__MEMORY.html

换上之后，仍然没有什么提高。



# 关于存储体冲突

bank-conflict:


##如何减少存储体冲突？


## 关于bank conflict的解释：

![](/images/cuda/bank-conflict.png)

一个块内的线程，最好相邻线程访问的是相邻的内存。否则容易bank conflict。


下面的介绍很好：（good！！）

http://blog.csdn.net/u013701860/article/details/50253343


