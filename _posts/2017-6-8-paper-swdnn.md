
layout:     post
title:      paper:swDNN:A Library for Accelerating Deep Learning Applications on
Sunway TaihuLight
keywords:   swDNNs
category:   [paper]
tags:       [paper]

## 出处：
2017年，IPDPS(CCF, B) 清华大学Haohuan Fu组

## 要解决的问题：

在sw26010的4个CG（260 cores）上实现了并行的CNN的训练过程（基本的primitives）。



## 摘要：
1. derive a performance model that guides us in the process of identifying the
most suitable approach for mapping the convolutional neural
networks (CNNs) onto the 260 cores within the chip.

2. performing a systematic optimization that explores major factors，
such as organization of convolution loops, blocking techniques,
register data communication schemes, as well as reordering
strategies for the two pipelines of instructions.

3. 获得的性能情况：
（1）achieve a double-precision performance over 1.6 Tflops for
the convolution kernel, achieving 54% of the theoretical peak.
（2）Compared with Tesla K40m with cuDNNv5, swDNN results in 1.91-9.75x performance speedup in an evaluation with over 100 parameter configurations.

## 主要贡献
（1）基于对DNN算法和对sw26010体系结构的分析，我们探索出了一个性能模型，他可以：
demonstrate影响性能的major factors；指导我们不同问题规模下，算法与底层硬件如何映射。
（2）量身定做了一个寄存器通信scheme：最大化卷积kernel的data reuse(reduces the memory bandwidth requirement for almost an order of magnitude)
 (3)design of the most suitable pipelining of instructions that reduces the idling time of computation units by maximizing the overlap of memory operation instructions and computation instructions.(指令重排，充分利用双流水线)
 

## 主要内容
第三节：MAPPING CNN TO SW26010: A PERFORMANCE MODEL
A. CNN简介：介绍了它的7层循环的伪代码
B. The SW26010 Many-Core Processor:
（1）sw的基本情况；
（2）sw与其他处理器不同的特征：

64KB Local directive Memory (LDM) (also known as Scratch Pad Memory (SPM)) as a user-controlled fast buffer；
The 8 column and row communication buses enable fast register communication channels
across the 8 by 8 CPE mesh，提供过来一种CPE级数据共享的高效方式；
每个CPE有2个流水线，把2条流水线用起来。identifying the right form of instruction-level parallelism can potentially resolve the dependences in the instruction sequences, and further improve the computation throughput；

C. The challenges for mapping CNN to SW26010
（1）首先，计算CNN有2种方法：空域里的GEMM的方法；频域里的FFT方法；鉴于后者对带宽的要求比较高，且需要全局通信。所以，本文选择GEMM的方法。
（2）the following major factors that may limit the performance of CNN on SW26010：

	(a)机器的计算能力，远远超过访存能力（相比GPU来说），所以，即使是计算占优的CNN，也需要好好设计访存模式来减少对内存带宽的约束；

 	(b)The algorithm of CNN involves all-to-all connections between inputs, filter kernels, and outputs. As a result, a parallel CNN design generally requires frequent data communication among different processing elements.所以，基于寄存器通信设计良好的数据共享很重要。

D. Performance model
这里我没有完全看懂。


## 第四节：LDM-RELATED OPTIMIZATIONS

## 第五节：REGISTER-RELATED OPTIMIZATIONS

##  第六节：INSTRUCTION REORDERING
（这一节我看懂啦。）
### A. Instruction Pipelines
对sw上的双指令流水线进行介绍，并说明双流水线对指令重排的要求：尽量的让浮点运算流水线P1上只执行浮点运算，提高计算性能，把既可以在P0，又可以在P1流水线上执行的整数运算指令放到P0上执行。（我之前也是这么做的）
#### 我学到了一个新的知识点（之前我只注意了第3条）：
The two execution pipelines share an Instruction Decoder (ID), and an instruction queue is maintained in the ID stage. In each cycle（每一拍）, two instructions in the front of the queue are checked by the ID and can be issued into two pipelines simultaneously if all the following conditions are satisfied:

	1) Both instructions have no conflicts with the unfinished instructions issued before.（冲突指哪些？）
	2) The two instructions have no Read After Write (RAW) or Write After Write (WAW) conflicts.
	3) The two instructions can be handled by two execution pipelines separately。

### B. Instruction Reordering Optimization
#### 指导指令重排的几步：
1) Dependence analysis
*第一*：load指令的延迟是4拍，浮点运算延迟7拍，所以浮点运算与跟它的操作数的取指令之间，要至少隔开4拍。
第二：计算指令与计算指令之间有没有依赖。gemm是没有的。
分析其他程序的时候这点是要特别注意的。有时候这种依赖是排不开的。（我加的这句）
2) Intra-loop pipelining and reordering
最内层kernel的指令重排。参看Figure 6（确实是排开了，并且利用好了双流水线。）
3) Inter-loop pipelining and reordering
内层循环外面的头和尾。
在2）的前提上，处理头部和尾部。因为2）里面为了把计算与访存盖住，把最原始的取数计算给打乱了。需要头部先取5个数，然后尾部把2）中最后一次循环没有处理完的计算处理完。（我用过）

## performance
1.卷积kernel的计算达到了计算峰值的54%。
2.比较对象是GPU平台上的cuDNN。（比GFLOPS）
3.只是测试了卷积部分的性能。DNN中整个训练过程是没有测试的。
4.验证了一下提出的性能模型。看实际达到的Gflops与性能预测出来的差距大不大。

## 我的评价（论文值得学习的地方）
1.性能模型建模那里，我没有正在看懂。还需要细细想想。
2.本文使用的优化技巧都不是新的，我都接触过。但是如何把这些方法的参数量化，与性能模型结合起来，有点难度，因为对硬件的理解不够深刻。
3. 

