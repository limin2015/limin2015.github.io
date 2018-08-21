---
layout: post
title:  CUDA性能优化-如何确定块数，和块内线程数
keywords: CUDA
categories : [CUDA]
tags : [CUDA编程]
---


探索开启kernel时，如何设置每一块中的线程数，和每个grid中的块数。以及active-block和active-threads是多少。


# 1. 确定每一块中的线程数，和每个grid中的块数的原则是什么？

1.1  active-thread和active-block是如何计算出来的？

这是通过设备属性查询出来的值：


    Total amount of constant memory:               65536 bytes
    Total amount of shared memory per block:       49152 bytes
    Total number of registers available per block: 65536
    Warp size:                                     32
    Maximum number of threads per multiprocessor:  2048
    Maximum number of threads per block:           1024


（1）若一个block开256（**程序员设置的**）个线程，每个线程使用a个寄存器（程序写好后，可以数出来，程序的特点），
一个SM总共有**b**（硬件的特点）个寄存器，
那么受寄存器总数的影响，活跃的线程数为active-thead = b/a个，活动的active-block= b/a/256。同时也可算出活跃的
warp数是多少。

注意：这里是根据寄存器资源进行的计算，也可以根据每个线程使用share-mem的资源情况，进行计算。

（2）关于warp调度时的隐藏访存延迟：

gpu硬件通过warp的time-slice的调度来达到隐藏一些warp的访存延迟的效果。

（a）为一个warp中的所有线程分发一条新的指令，需要4个cycle（时钟周期）；访问global-mem需要400个cycle，
 那么至少需要（400/4）个active-warp (TODO)


# 2. gpu的Occupancy（TODO）

2.1. 什么是occupancy？

Occupancy的定义：活动的warp数量与最大数量的比值。 

最大数量计算公式：

maxWarps = prop.maxThreadsPerMultiProcessor / prop.warpSize;

活动的warp数量通过公式计算出来：见1.1和2.2(2)


引自：[CUDA总结：Occupancy](http://blog.csdn.net/kelvin_yan/article/details/54343646)



2.2. nvidia的sample的SDK中有一个occupancy的计算工具：
    NVIDIA_CUDA-8.0_Samples/0_Simple/simpleOccupancy

内部有两个函数：[nvidia-doc](http://docs.nvidia.com/cuda/cuda-runtime-api/group__CUDART__HIGHLEVEL.html#group__CUDART__HIGHLEVEL_1g5a5d67a3c907371559)ba692195e8a38c

	（1）cudaOccupancyMaxPotentialBlockSize( int* minGridSize, int* blockSize, T func, UnaryFunction blockSizeToDynamicSMemSize, int  blockSizeLimit = 0, unsigned int  flags = 0 )

Returns in *minGridSize and *blocksize a suggested grid / block size pair that achieves the best potential occupancy (i.e. the maximum number of active warps with the smallest number of blocks). 

返回值是前两个参数。根据func函数（写好的一个global函数），返回一组kernel函数的设置，即块内线程数，块数大小，使得获得最好的occupancy。


	（2）cudaOccupancyMaxActiveBlocksPerMultiprocessor( int* numBlocks, T func, int  blockSize, size_t dynamicSMemSize )

Returns in *numBlocks the maximum number of active blocks per streaming multiprocessor for the device function. 

返回值是numBlocks；剩下的是输入值；根据func函数中设置的blocksize和使用的dynamicSMemSize（动态share-mem的大小），来计算active-block的大小。



# 理解一下下面的两句话

（1）too much shared memory allocated to one block limits the number of active blocks per multiprocessor:
若一个块内分配的shmem太多，则活跃的块数就会受限制。



（2） 寄存器使用过多成为CUDA程序瓶颈的情况分析：（还没看）

http://blog.csdn.net/u013443737/article/details/23422569



# decide maximum active threads and maximum active  block


**计算**：判断一个块中的active threads和active  block是多少。

（1）如果一个 thread 要用到 16 个 register 的话(在 kernel 中宣告的变量)，那一个 SM 的 8192 个 register 实际上只能让 512 个 thread 来使用。（决定了active threads的数目）

（2）shared memory 由于是 thread block 共享的，因此变成是要看一个 block 要用多少的 shread memory、一个 SM 的 16KB 能分给多少个 block 了。 （决定了一个SM中的active block的数目）







