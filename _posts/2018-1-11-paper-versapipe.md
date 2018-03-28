---
layout:     post
title:      paper-VersaPipe A Versatile Programming Framework for Pipelined Computing on GPU
keywords:   paper-VersaPipe-2017
category:   [paper]
tags:       [paper]
---


# 出处：
2017年，MICRO（ccf-a）


# 摘要

1. provides a systematic examination of various existing pipeline execution models on GPU, and analyzes their strengths and weaknesses
2. proposes three new execution models equipped with much improved controllability, including a hybrid model that is capable of getting the strengths of all. 并将这些模型写进了一个库里：versapipe.
3. VersaPipe produces up to 6.90× (2.88× on average) speedups over the original manual implementations.


# 疑问

Pipeline parallel programming:是什么？？


concurrent kernel execution:(CKE) 如何理解？？（开启的多个kernel，可能会被同时调度到不同的SM上执行）

连续启动多个kernel，当还有硬件资源时，当前面的kernel还在执行的时候，就可以“同时”执行另一个kernel。（异步执行）

//TODO:

如果有两个kernel(kernel1,kernel2)，可是kernel2需要kernel1运算完的数据(存在global memory)，如果两个同时跑的话，显卡会如何执行kernel呢? 

(CKE) can run more than one kernels at the same time, it is limited to the case in which the previous kernels do not fully utilize all the resources (SMs) in the GPU and the current kernel is not dependent on them. 

This allows for a limited form of task-parallel execution on GPU, but a task must be described in a separate kernel, which incurs overhead, makes GPU underutilized for kernels with small workload and usually cannot maintain good data locality as the binding of a task onto an SM cannot be controlled. （任务不能绑定到特定的SM上，是被硬件自动调度的。）

这让我想到了hyper-Q技术：有啥异同？




# introduction：

1. 之前，大部分人主要通过：megakernel的方式：所有的stages被放到一个kernel中，然后根据当前是第几个stage，来选择执行kernel函数中的哪个分支。 具体的，是通过：launch as many blocks as can be concurrently scheduled on GPU and schedule the tasks through software managed task queues.

缺点： 大的kernel，导致寄存器使用量很多，这会导致同时并行执行的线程数降低，=》并行度降低。

2. 还有，之前的工作，都把任务，线程的调度（when and where (on which computing unit of a GPU) a GPU thread runs）全部交给gpu来做。
但其实，可以采取software的方法，解除这个限制。  
本文combining two recent software techniques (persistent threads [3] and SM-centric method [50]) to circumvente the limitation.


# persistent thread

理解一下下面的解释：

In the persistent thread technique, the kernel creates a number of threads that stay alive throughout the execution of a kernel function, usually through the use of a while loop in the kernel as Figure 3(c) illustrates. These threads continuously fetch new data items from the queue of each stage and execute the corresponding stage based on data items they fetched. These threads are called persistent threads.



# SM-centric method:

cess a data item in a pipeline stage) of a GPU kerenl to the GPU SMs. It is through transforming the kernel code such that each GPU thread decides which tasks to process based on the ID of the SM on which the thread runs. More specifically, it uses a method called SM-based task selection to guarantee task execution is based on a specific SM and enable the binding between tasks and SMs, and uses a filling-retreating scheme to offer a flexible control of the amount of active threads on an SM.



## dynamic parallelism：

Dynamic Parallelism (DP) allows threads running on GPU to launch subkernels。



# 已有的gpu上pipeline程序的执行模型

前两个是使用的gpu默认的编程模型；后一个是带有软件调度策略的method。

## run to complete(RTC)

为所有的stages开一个kernel，然后在每一个SM上，依次执行所有的stage。（paper中说：对于没有recursive和全部同步的流水线程序来说，这个方法在gpu上很好实现。）


## kernel by kernel(KBK)

开启多个kernel，一个kernel代表pipeline 程序中的一个或者多个stages。然后执行即可。（这个方法可以将任意的pipeline的程序实现在gpu上。）

## megakernel:

为所有的stages开一个大的kernel，使用software scheduler调度每一个阶段。通过使用persistent thread来实现。



