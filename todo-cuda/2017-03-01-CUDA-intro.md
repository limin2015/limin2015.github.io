---
layout:     post
title:      CUDA的简单介绍
keywords:   安装、架构介绍、常用函数库
category:   CUDA
tags:		[CUDA编程]
---

前言：
GPU作为如今主流的异构计算平台，收到越来越多的追捧，尤其是深度学习的发展，更加催生了其应用。作为并行计算领域的一枚，必须要好好学习一番啦。


# GPU各种架构、型号整理
 
## NVIDIA 图形处理器命名规则

    •GPU体系结构代号
        –代表不同的微体系结构
        –如：Fermi、Kepler、Maxwell、Pascal、Volta
    •GPU产品线代号
        –代表不同的显卡产品系列
        –如：GeForce、Quadro、Tesla分别对应个人计算机、高性能图形工作站和高性能通用计算
    •显卡产品型号
        –代表具体产品配置
        –如：GF100表示采用Fermi架构的GeForce系列显卡

## 架构整理

1. 每种架构的大致情况：

GTX 280：

Fermi:supports concurrent kernel execution，

Kepler:introducing the Hyper-Q feature，

maxwell:

pascal:

    P40:2016年发布，专为神经网络推理，支持TensorRT。

    P100：

Volta:

    Tesla V100



2. 几种架构对比
    （1） 计算能力的对比：

        Fermi   - NVIDIA compute capability 2.x cards
        Kepler  - NVIDIA compute capability 3.x cards
        Maxwell - NVIDIA compute capability 5.x cards
        Pascal  - NVIDIA compute capability 6.x cards
        Volta   - NVIDIA compute capability 7.x cards

    

GeForce、Quadro、Tesla分别对应个人计算机、高性能图形工作站和高性能通用计算。

Tesla:K40, K80, P4, P40 and so on.
GeForce(GTX Tian):



总结（几种gpu的对比）：

https://www.cnblogs.com/lijingcong/p/4958617.html

http://we.poppur.com/thread-2367589-1-1.html



参加讲座时的问题：

1. 我们都知道nvidia的GPU的架构和产品都更新的很快，接触的比较少的人，可能都不是特别了解其发展，易老师可否帮忙梳理一下，尤其是一些关键技术出现的架构。

    答1. 正如我在PPT介绍的一样，nvidia GPU经过了10多年的发展，从早期的G80，GT200架构的GPU，到2010年发布fermi架构，这是一个较大的飞跃，第一个完整的GPU计算架构，也确定了基本的GPU架构路线，后来陆续发布的Kepler架构，Maxwell架构，Pascal架构，Volta架构。


    早期G80,GT200对应的GPU产品有C870,C1060，C1070等，fermi架构，常见的产品有C2050，C2070，M2070，M2090等，Kepler架构大家应该比较熟悉了，有K20,K40,K80等；Maxwell架构有M10,M40,M60等，Pascal架构有P4,P40,P100，Volta架构只有一款，就是V100。


    这些架构有什么区别？
    不同的架构首先制程不同，比如V100采用的是10nm制程，其次是fp64,fp32,int32核心的主频和核心数不同，V100增加了tensor core 核心，这也是架构的不同，另外，L1,L2 cache，register寄存器数量，不同架构也是不同的。


2. 可否介绍一下，cuda对于任务并行的支持情况？如果想实现任务的并行，目前有哪些方法？

    答2. GPU的并行包括thead级别，即GPU线程的并行；更高层次是kernel级别的并行。Thead并行体现在，我们在执行一段程序代码时，可以使用单指令多线程（SIMT）来管理和执行线程，支持成百上千的线程并发执行，这里只有一个kernel在运行。如果要实现多个kernel并行，可以通过stream来实现了，可以通过MPS多进程服务，以前叫Hyper-Q，来实现多个stream的调度，不同的stream实现不同的任务。

    如果只是想在一个GPU上运行多个GPU应用，比如同时提交amber，Gromacs作业，这个也是可以的。如果GPU的利用率不高，这样做没问题，如果GPU利用率已经是100%，运行多个作业会导致计算速度变慢。如果使用slurm调度，它只会给空闲的GPU资源分配任务。

3. 大型HPC应用在gpu上加速时的一些经验

（1）先要梳理代码，在串行代码的基础上，对原有代码进行适当修改，使得易于并行。梳理的时候，把每一个模块的并行模式，计算模式梳理清楚。（前面梳理不清，也不利于后面调试正确性）

（2）正确性的测试：要一个模块一个模块的进行测试。

参考：[清华大学计算机系副教授都志辉主讲的天气预报程序在GPU上的移植]https://mp.weixin.qq.com/s?__biz=MzA4MTQ4NjQzMw==&mid=2652712916&idx=2&sn=4023383c1b4627299cb50e0c93be9ffb&chksm=847db8dab30a31cc1cf9714a2e7d69d130420c431a5da921d21fb5135425fbf326c6a01c36ab&scene=0&pass_ticket=TGzlhjs6V8afDTMceHN074xawSXdg0SRnDXKSdH3zy%2BpChYmlbTugx%2BRch7iKtZP#rd


     

# gpu上的一些高性能的函数库：

cublas：

cuDNN:

thrust：

NPP：

CULA：基于CUDA的一个lapack库。



cutlass：基于模板的一个gemm库，需要整理一下它的并行算法，设计思想。


# gpu的任务并行和数据并行，指令并行分别指什么？

1. For Ivy Bridge and MIC （多核和众核系统）, the task parallelism is achieved by utilizing
multiple hardware threads. For MIC, the data parallelism benefits
from on-core VPU (Vector Processing Unit) and SIMD. 

2. For Fermi and Kepler, the task parallelism comes from the independent warps
that are executed **by different SMs**（\red{really}）. 
In each warp, the data-parallelism
is achieved by the computations performed by the different CUDA
cores(SP) within the SM. In order to get satisfactory performance, fully
utilizing the two-level parallelism and improving the occupancy rate
of the computing resources are crucial.

3. 指令并行指什么？TODO



# 好的学习资料：

（1） NVIDIA官方的faq：（比如，关于线程数如何设置等问题）
	
	[NVIDIA官方的faq链接](https://developer.nvidia.com/cuda-faq)

（2）gpu官网上的一些资料（easy-reading）：
[even-easier-introduction-cuda](https://devblogs.nvidia.com/parallelforall/even-easier-introduction-cuda/)

[how-implement-performance-metrics-cuda-cc](https://devblogs.nvidia.com/parallelforall/how-implement-performance-metrics-cuda-cc/)

[how-query-device-properties-and-handle-errors-cuda-cc](https://devblogs.nvidia.com/parallelforall/how-query-device-properties-and-handle-errors-cuda-cc/)

[how-optimize-data-transfers-cuda-cc](https://devblogs.nvidia.com/parallelforall/how-optimize-data-transfers-cuda-cc/)

[how-optimize-data-transfers-cuda-cc](https://devblogs.nvidia.com/parallelforall/how-optimize-data-transfers-cuda-cc/)

[how-overlap-data-transfers-cuda-cc](https://devblogs.nvidia.com/parallelforall/how-overlap-data-transfers-cuda-cc/)

[如何使用好global memory？](https://devblogs.nvidia.com/parallelforall/how-access-global-memory-efficiently-cuda-c-kernels/)

[AXPY:](https://devblogs.nvidia.com/parallelforall/six-ways-saxpy/)

[风辰的 CUDA 入门教程](http://download.csdn.net/detail/fdp0525/5944705?locationNum=13&fps=1)
[子棐之GPGPU](https://mp.weixin.qq.com/s?__biz=MzI5ODk5NjQ3Mg==&mid=2247483967&idx=1&sn=39db52574e3623e01d505f087a86fef5&chksm=ec9c05a8dbeb8cbe4cdebafedafaf811436eb861b8a7541fede020e541808c1a310f05b45d2b&mpshare=1&scene=1&srcid=0513kFLQUKyFu2gts4t7l510&pass_ticket=0xD3gNGx0tmurjVLWXLN5ooqVqgUF%2BoFWOwGCbMXoJtDCkruWiSxKiFpiwjE5KtK#rd)



## 我的127服务器

### 基本信息： 

是Tesla K40m with compute capability 3.5

CUDA核心数量：2880

双精度浮点性能：1.43 Tflops，单精度浮点性能：4.29 Tflops（3:1）

显存总容量：12GB ； share-memory：

显存带宽: 288GB/s 支持PCI-E 3.0；  传输带宽从8GB/s（tesla k20）近乎翻番至15.75GB/s；

功耗：235W热设计功耗 被动散热

GPUBoost feature：其实就是可以设置clock frequency。

[是什么，如何开启？](http://blog.csdn.net/gold0523/article/details/52675708)


### 服务器上的一些命令：

    qnodes //查看所有的节点信息
    qnodes -q gpu03 //查看节点gpu03的一些信息（包括gpu占用率和显存使用量等）
    qstat           //查看当前作业提交情况
