---
layout:     post
title:      GPU上的任务并行
keywords:   stream, hyperQ
category:   CUDA
tags:		[CUDA编程]
---

主要介绍GPU上的任务并行相关的一些知识和技术。

# CUDA的stream

流技术是GPU上用来支持current kernel execution执行的一种技术。


## 一个问题

之前，和师弟讨论过一个问题，NVIDIA的current kernel execution，是不是不需要将每个kernel放到单独的流中，直接连续的spawn多个kernel，kernel就可以并发执行？

paper[Efficient Kernel Management on GPUs](http://xueshu.baidu.com/s?wd=paperuri:(95553d5d2aa62e7f7a47add23dabdd9c)&filter=sc_long_sign&sc_ks_para=q%3DEfficient+kernel+management+on+GPUs&tn=SE_baiduxueshu_c1gjeupa&ie=utf-8&sc_us=2527773259732545580)
中说current kernel execution是用stream技术来具体实现的。


## 单个stream的情况

http://blog.csdn.net/u010335328/article/details/52453499

看完上面的blog后，有个疑问，他实现的是不是就是双buffer啊？？（内部有依赖判断？？）

NOTE:

all GPU-related tasks placed in one stream (which is default behaviour) are executed sequentially.

## multi-stream

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


# 流技术与hyper-q（TODO）

[流技术与hyper-q区别和联系](http://blog.163.com/wujiaxing009@126/blog/static/71988399201712035958365/)



