---
layout:     post
title:      CUDA的stream(任务并行related)
keywords:   stream
category:   CUDA
tags:		[CUDA编程]
---


TODO: 介绍cuda stream技术。流技术是用来支持current kernel execution的。



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

1：一个SM中可能有128或者192个SP（根据compute capability不同），一个thread需要SP中运行，一个SM同时执行的只有一个warp也就是32个thread，那么这个SM中的其他SP都在空闲？


note:
每个SM包含的SP数量依据GPU架构而不同，Fermi架构GF100是32个，GF10X是48个，Kepler架构都是192个，Maxwell都是128个。

软件逻辑上是所有SP是并行的，但是物理上并不是所有SP都能同时执行计算，因为有些会处于挂起，就绪等其他状态，这有关GPU的线程调度.

答案：一个SM中的SP在物理上也是分组的。每一个组处理一个warp的操作。


kepler架构的一个SMX包涵192个sp及4warp+8dispatch，sp就算不异步，其运算能力也能满足4warp的指令，所以Shader分频被取消，即使有Shader分频，kepler的实际性能也不会提升，因为kepler的运算能力非常够了，瓶颈应该在线程调度单元了.




# 一个问题

之前，和师弟讨论过一个问题，NVIDIA的current kernel execution，是不是不需要将每个kernel放到单独的流中，直接连续的spawn多个kernel，kernel就可以并发执行？

paper[Efficient Kernel Management on GPUs](http://xueshu.baidu.com/s?wd=paperuri:(95553d5d2aa62e7f7a47add23dabdd9c)&filter=sc_long_sign&sc_ks_para=q%3DEfficient+kernel+management+on+GPUs&tn=SE_baiduxueshu_c1gjeupa&ie=utf-8&sc_us=2527773259732545580)
中说current kernel execution是用stream技术来具体实现的。


# 单个stream的情况

http://blog.csdn.net/u010335328/article/details/52453499

看完上面的blog后，有个疑问，他实现的是不是就是双buffer啊？？（内部有依赖判断？？）



# multi-stream

下面的这个解释很棒：
http://blog.163.com/wujiaxing009@126/blog/static/71988399201712035958365/

我有几个疑问：

1. 在多stream的程序中，存在着false dependcy的问题。如下的代码，在具体调度的时候，到底是怎么样的？
   
    for (int i = 0; i < nStreams; i++) 
    {
        int offset = i * bytesPerStream;
        cudaMemcpyAsync(&d_a[offset], &a[offset], bytePerStream, streams[i]);
        kernel<<grid, block, 0, streams[i]>>(&d_a[offset]);
        cudaMemcpyAsync(&a[offset], &d_a[offset], bytesPerStream, streams[i]);
    }

    答：在物理层面上，所有stream是被塞进硬件上唯一一个工作队列来调度的，当选中一个grid来执行时，runtime会查看task的依赖关系，如果当前task依赖前面的task，该task就会阻塞，由于只有一个队列，后面的都会跟着等待，即使后面的task是别的stream上的任务。如下图所示：
    
    ![](/images/cuda/stream-1.png)

    从图中可以看出：C和P以及R和X是可以并行的，因为它们在不同的stream中，但是ABC，PQR以及XYZ却不行，比如，在B没完成之前，C和P都必须等待。
    
    **那么是不是**：真正的执行时这样的：(这样的话，感觉啥也没有掩盖了，C和P的并行执行，其实都是数据传输，得有2条PCI-E总线，才可以真正并行，或者先P，再C，才能获得一些性能提升。)
    
        A->B->C
              P->Q->R
                  X->Y->Z

    其实也就是说：大部分时候还是不能并行执行的。上一个kernel的计算和当前kernel计算是不是不能并发执行啊？？？

   **hyper-Q**可以用来解决上面提到的伪依赖问题。



2. 多个stream中的多个操作，到底是重叠的（**重叠行为分析**）？？

(1) 在下面的页面搜索：Overlapping Behavior

[Overlapping Behavior]{http://docs.nvidia.com/cuda/cuda-c-programming-guide/#creation-and-destruction-streams)

    The amount of execution overlap between two streams depends on **the order in which the commands are issued to each stream and whether or not the device supports overlap of data transfer and kernel execution** (see **Overlap of Data Transfer and Kernel Execution**), concurrent kernel execution (see **Concurrent Kernel Execution**), and/or concurrent data transfers (see **oncurrent Data Transfers**).

(2) 具体分析：

        eg：
        cudaStream_t stream[2]; 
        for (int i = 0; i < 2; ++i) 
            cudaStreamCreate(&stream[i]); 
        float* hostPtr; 
        cudaMallocHost(&hostPtr, 2 * size);

        for (int i = 0; i < 2; ++i) { 
            cudaMemcpyAsync(inputDevPtr + i * size, hostPtr + i * size, size, cudaMemcpyHostToDevice, stream[i]); 
            MyKernel <<<100, 512, 0, stream[i]>>> (outputDevPtr + i * size, inputDevPtr + i * size, size); 
            cudaMemcpyAsync(hostPtr + i * size, outputDevPtr + i * size, size, cudaMemcpyDeviceToHost, stream[i]); 
        }

        （a）若不支持current Data Transfers，则，以上的代码，没有overlap；
        （b）若支持current Data Transfers，则，stream[0]的memcpydevice2host和stream[1]的memcpyhost2device重叠起来；
        （c）不管支持不支持其他的，其他的overlap都没有。

        eg：
        for (int i = 0; i < 2; ++i) 
            cudaMemcpyAsync(inputDevPtr + i * size, hostPtr + i * size, size, cudaMemcpyHostToDevice, stream[i]); 
        for (int i = 0; i < 2; ++i) 
            MyKernel<<<100, 512, 0, stream[i]>>> (outputDevPtr + i * size, inputDevPtr + i * size, size); 
        for (int i = 0; i < 2; ++i) 
            cudaMemcpyAsync(hostPtr + i * size, outputDevPtr + i * size, size, cudaMemcpyDeviceToHost, stream[i]);

        （a）这个代码，若支持Overlap of Data Transfer and Kernel Execution，则，传1和算0是overlap的，算1和传回0是overlap的；
        （b）若支持concurrent kernel execution，则，算0和算1也会重叠一部分（咋重叠？？）


3. 在判断哪些能够overlap时候，还有一些**隐式同步**的限制：**TODO**(我没有看懂！！)

    ![](/images/cuda/stream-1.png)





#  cublas中的gemm是不是不支持stream啊？因为没有提供stream这个参数

支持。

[can be solved by call a routine](http://docs.nvidia.com/cuda/cublas/#parallelism-with-streams)


        If the application uses the results computed by multiple independent tasks, CUDA™ streams can be used to overlap the computation performed in these tasks. 

        The application can conceptually associate each stream with each task. In order to achieve the overlap of computation between the tasks, the user should create CUDA™ streams using the function cudaStreamCreate() and set the stream to be used by each individual cuBLAS library routine by calling cublasSetStream() just before calling the actual cuBLAS routine. Then, the computation performed in separate streams would be overlapped automatically when possible on the GPU. This approach is especially useful when the computation performed by a single task is relatively small and is not enough to fill the GPU with work. 

        We recommend using the new cuBLAS API with scalar parameters and results passed by reference in the device memory to achieve maximum overlap of the computation when using streams. 


        Read more at: http://docs.nvidia.com/cuda/cublas/index.html#ixzz54JN8KiZb 
        Follow us: @GPUComputing on Twitter | NVIDIA on Facebook


# cudaMemcpyAsync：异步传输

注意用于异步传输的数组，必须是in page-locked memory（内存空间是物理地址，没有对应的虚拟地址。）



# cudaMemcpyToSymbol有没有异步的函数


在下面的页面可以搜到：cudaMemcpyToSymbolAsync //Copies data to the given symbol on the device

    http://docs.nvidia.com/cuda/cuda-runtime-api/group__CUDART__MEMORY.html

换上之后，仍然没有什么提高。
