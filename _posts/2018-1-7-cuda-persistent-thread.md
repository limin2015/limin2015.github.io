---
layout:     post
title:      CUDA的persistent thread（永久线程）
keywords:   stream
category:   CUDA
tags:		[CUDA编程]
---


这个需要调研一下：很多paper中提及了的。


找个代码看看！！

# gpu的block的调度（硬件角度）

[ref](http://blog.csdn.net/GH234505/article/details/51115994)

每一个block被分配到一个特定的SM上，（最好保证线程块的数目是SM数目的整数倍，以此提高设备的利用率。）
block一旦被分配到一个SM中，该block就会一直驻留在该SM中，直到执行结束。
不同块（分配到SM中）之间的执行没有顺序，完全并行。

具体如何把block分配到SM上呢：

任务分配单元（warp调度器）使用的是轮询策略：轮询查看SM是否还有足够的资源来执行新的块，如果有则给SM分配一个新的块，如果没有则查看下一个SM。决定能否分配的因素有：每个块使用的共享存储器数量，每个块使用的寄存器数量，以及其它的一些限制条件。任务分配单元在SM的任务分配中保持平衡，但是程序员可以通过更改块内线程数，每个线程使用的寄存器数和共享存储器数来隐式的控制，从而保证SM之间的任务均衡。


同一线程块中的线程需要SM中的共享存储器共享数据，因此它们必须在同一个SM中发射。线程块中的每一个线程被发射到一个SP上。
任务分配单元可以为每个SM分配最多8个块（啥意思？？？）。而SM中的线程调度单元又将分配到的块进行细分，将其中的线程组织成更小的结构，称为线程束（warp）。在CUDA中，warp对程序员来说是透明的，它的大小可能会随着硬件的发展发生变化，在当前版本的CUDA中，每个warp是由32个线程组成的。SM中一条指令的延迟最小为4个指令周期。8个SP采用了发射一次指令，执行4次的流水线结构。所以由32个线程组成的Warp是CUDA程序执行的最小单位，并且同一个warp是严格串行的，因此在warp内是无须同步的。在一个SM中可能同时有来自不同块的warp。当一个块中的warp在进行访存或者同步等高延迟操作时，另一个块可以占用SM中的计算资源。这样，在SM内就实现了简单的乱序执行。



## warp:

1. warp vote: 快速的进行 warp 内的简单统计

2.基本上 warp 分组的动作是由 SM 自动进行的，会以连续的方式来做分组。比如说如果有一个 block 里有 128 个 thread 的话，就会被分成四组 warp，第 0-31 个 thread 会是 warp 1、32-63 是 warp 2、64-95 是 warp 3、96-127 是 warp 4。

每发出一条指令时，SIMT单元都会选择一个已准备好执行的warp块，并将指令发送到该warp块的活动线程。Warp块每次执行一条通用指令，因此在warp块的全部32个线程执行同一条路径时，可达到最高效率。如果一个warp块的线程通过独立于数据的条件分支而分散，warp块将连续执行所使用的各分支路径，而禁用未在此路径上的线程，完成所有路径时，线程重新汇聚到同一执行路径下，其执行时间为各时间总和。分支仅在warp块内出现，不同的warp块总是独立执行的–无论它们执行的是通用的代码路径还是彼此无关的代码路径。



3.一个 SM 一次只会执行一个 block 里的一个 warp，但是 SM 不见得会一次就把这个 warp 的所有指令都执行完;当遇到正在执行的 warp 需要等待的时候(例如存取 global memory 就会要等好一段时间)，就切换到别的 warp 来继续做运算，藉此避免为了等待而浪费时间。所以理论上效率最好的状况，就是在 SM 中有够多的 warp 可以切换，让在执行的时候，不会有「所有 warp 都要等待的情形发生;因为当所有的 warp 都要等待时，就会变成 SM 无事可做的状况了.



一个 SM 可以同时处理多个 thread block，当其中有 block 的所有 thread 都处理完后，他就会再去找其他还没处理的 block 来处理。假设有 16 个 SM、64 个 block、每个 SM 可以同时处理三个 block 的话，那一开始执行时，device 就会同时处理 48 个 block;而剩下的 16 个 block 则会等 SM 有处理完 block 后，再进到 SM 中处理，直到所有 block 都处理结束。 

## **我的疑问**：为什么SM中最多一次可以处理3个block？？？由硬件中的什么决定的？？



4.当一个 SM 里的 thread 越多时，越能隐藏 latency，但是也会让每个 thread 能使用的资源更少，因为share-memory和寄存器在一个SM上是有限的。


4.warp 是 CUDA 中，每一个 SM 执行的最小单位;如果 GPU 有 16 组 SM 的话，也就代表他真正在执行的 thread 数目会是 32x16 个。不过由于 CUDA 是要透过 warp 的切换来隐藏 thread 的延迟、等待，来达到大量平行化的目的，所以会用所谓的 active thread 这个名词来代表一个 SM 里同时可以处理的 thread 数目。 


5.warp divegence:

避免同一个warp存在不同的执行路径.(也就是说块内的线程，以32为一组，每个组中的线程执行相同的指令（最好没有分之）).


## 问题：


1.**计算**：判断一个块中的active threads和active  block是多少。

（1）如果一个 thread 要用到 16 个 register 的话(在 kernel 中宣告的变量)，那一个 SM 的 8192 个 register 实际上只能让 512 个 thread 来使用。（决定了active threads的数目）

（2）shared memory 由于是 thread block 共享的，因此变成是要看一个 block 要用多少的 shread memory、一个 SM 的 16KB 能分给多少个 block 了。 （决定了一个SM中的active block的数目）





2：一个SM中可能有128或者192个SP（根据compute capability不同），一个thread需要SP中运行，一个SM同时执行的只有一个warp也就是32个thread，那么这个SM中的其他SP都在空闲？


note:
每个SM包含的SP数量依据GPU架构而不同，Fermi架构GF100是32个，GF10X是48个，Kepler架构都是192个，Maxwell都是128个。

软件逻辑上是所有SP是并行的，但是物理上并不是所有SP都能同时执行计算，因为有些会处于挂起，就绪等其他状态，这有关GPU的线程调度.

答案：一个SM中的SP在物理上也是分组的。每一个组处理一个warp的操作。


kepler架构的一个SMX包涵192个sp及4warp+8dispatch，sp就算不异步，其运算能力也能满足4warp的指令，所以Shader分频被取消，即使有Shader分频，kepler的实际性能也不会提升，因为kepler的运算能力非常够了，瓶颈应该在线程调度单元了.





# persistent thread programming style:

[A Study of Persistent Threads Style GPU Programming for GPGPU Workloads](http://xueshu.baidu.com/s?wd=paperuri%3A%287ce95fb005239e06e86c2634b147f940%29&filter=sc_long_sign&tn=SE_xueshusource_2kduw22v&sc_vurl=http%3A%2F%2Fieeexplore.ieee.org%2Fxpls%2Fabs_all.jsp%3Farnumber%3D6339596&ie=utf-8&sc_us=10768365825906481192)

思想：相当于在software层面上，实现了任务和block的绑定。

**那么有什么好处呢，多哪种workload会产生好的结果呢？？**


两步：（没大懂！！）

1. Maximal Launch: A kernel uses at most as many blocks as can be concurrently scheduled on the SM:

Since each thread remains persistent throughout the execution of a kernel, and is active across traditional block boundaries until no work remains, the program- mer schedules only as many threads as the GPU SMs can concurrently run. This represents the upper bound on the number of threads with which a kernel can launch. The lower bound can be as small as the num- ber of threads required to launch a single block. 

2. Software schedules work through work queues, not hardware:

The traditional programming environment does not expose the hardware scheduler to the programmer, thus limiting the ability to exploit workload communication patterns. In contrast, the PT style bypasses the hard- ware scheduler by relying on a work queue of all blocks that are to be processed for kernel execution to com- plete. When a block finishes, it checks the queue for more work and continues doing so until no work is left, at which point the block retires.


