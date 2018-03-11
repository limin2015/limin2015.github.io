---
layout: post
title:  CUDA性能优化-shuffle指令和warp相关的指令
keywords: CUDA
categories : [CUDA]
tags : [CUDA编程]
---

整理一下用到的shuffle指令和warp相关的指令。

#shuffle指令功能：

shuffle指令，允许thread直接读其他thread的寄存器值，前提是两个thread在 同一个warp中。


## __shfl

下面的两个blog中的例子不错：

https://www.cnblogs.com/1024incn/p/4706215.html

http://blog.csdn.net/lingerlanlan/article/details/25401565


int __shfl(int var, int srcLane, int width=warpSize);

int __shfl_up(int var, unsigned int delta, int width=warpSize)

int __shfl_down(int var, unsigned int delta, int width=warpSize)

int __shfl_xor(int var, int laneMask, int width=warpSize)






## ref

https://www.cnblogs.com/1024incn/p/4706215.html

http://blog.csdn.net/lingerlanlan/article/details/25401565


# warp相关的指令：


1. warp-aggregated atomics技术：

    a useful technique to improve performance when many threads atomically add to a single counter. In warp aggregation, the threads of a warp first compute a total increment among themselves, and then elect a single thread to atomically add the increment to a global counter. 

[nvidia's intro](https://devblogs.nvidia.com/cuda-pro-tip-optimized-filtering-warp-aggregated-atomics/)


注意，下面的几个NVIDIA的文档非常的好：有空的时候整理出来

[GPU Pro Tip: Fast Histograms Using Shared Atomics on Maxwell](https://devblogs.nvidia.com/gpu-pro-tip-fast-histograms-using-shared-atomics-maxwell/)
[Faster Parallel Reductions on Kepler](https://devblogs.nvidia.com/faster-parallel-reductions-kepler/)
[Voting and Shuffling to Optimize Atomic Operations](https://devblogs.nvidia.com/voting-and-shuffling-optimize-atomic-operations/)
[CUDA Pro Tip: Occupancy API Simplifies Launch Configuration](https://devblogs.nvidia.com/cuda-pro-tip-occupancy-api-simplifies-launch-configuration/)
[CUDA Pro Tip: Increase Performance with Vectorized Memory Access](https://devblogs.nvidia.com/cuda-pro-tip-increase-performance-with-vectorized-memory-access/)
[CUDA Pro Tip: Profiling MPI Applications](https://devblogs.nvidia.com/cuda-pro-tip-profiling-mpi-applications/)


2. 束表决函数：简单的理解就是在一个warp内进行表决

http://blog.csdn.net/u010646276/article/details/46804545

    __all(int predicate)：指的是predicate与0进行比较，如果当前线程所在的Wrap所有线程对应predicate不为0，则返回1。
    __any(int predicate)：指的是predicate与0进行比较，如果当前线程所在的Wrap有一个线程对应的predicate值不为0，则返回1。
    __ballot(int predicate)：指的是当前线程所在的Wrap中第N个线程对应的predicate值不为0，则将整数0的第N位进行置位。






# 位操作：（TODO：需要整理到别的blog中）

        置位可以用或操作符“|”实现：y = x | (1 << n)    对x的第n位进行置位（置为1）
        清除可以用与操作符”&“实现：y = x & (~(1 << n)) 对x的第n位清除（置为0）
        取反可以用异或操作符”^“实现： y = x ^ (1 << n) 对x的第n位取反
        Bit提取操作： bit = (x | (1 << n)) >> n;      提取x的第n位的值