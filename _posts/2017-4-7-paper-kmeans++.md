---
layout:     post
title:      paper-Parallel k-means++ for Multiple Shared-Memory Architectures
keywords:   kmeans++ optimization
category:   [paper]
tags:       [paper]
---

## 出处：
2016年，ICPP

## 要解决的问题：
1. 之前的工作只关注近似kmeans++的并行化，本文提出了一个精确kmeans++求解的并行化算法，
并给出了正确性证明。
2. kmeans++算法包括初始化选取和聚类2部分。本文只并行化了中心点初始化这个kernel。因为后者已经被优化的比较多啦。初始化步骤没有被优化过，在并行环境下，它成为了性能瓶颈（相比优化后的聚类操作）。

## 摘要：
1.  在三种不同的共享内存架构上实现了并行化：multicore CPU, high performance GPU, and the
massively multithreaded Cray XMT platform 。并demonstrate各个平台上的scalability。

2. 建立了一个线性回归模型，分析在哪个输入规模下，哪个平台运行效果更好一些。并提出了一个可视化方法，可以看某一规模下，在哪个平台上，速度最快。


## 前人工作
1. [7]， GPU， only parallelizes the calculation of distances of data points to each seed。
平台：Intel Core 2 Duo 2.2GHz processor and a Nvidia GeForce 9600M GT graphics card
效果：5X speedup（相比cpu版本。）

2. [12]， 本文说kmeans++初始化方法是天然串行的，故，他们用MapReduce提供了一个different k-means initialization technique，实现了他们自己的算法：k-means||。
缺点：1）至于中心点随机初始化方式的算法进行了对比。但是因为迭代次数不一样，结果并不能说明他们的并行效果好。
	 2）没有说明k-means|| 的效果（可拓展性）for an increasing number of processors。
3. [15],[16]都是用mapreduce做的:kmeans++近似算法的并行化。

4. [17]提出了一个精确kmeans++的并行算法：它的方法，与我们的多核平台上的并行化思路很相近，同样的，leaves the final step of selecting a seed to be performed in serial. 但是这种方法只对线程数相对少的时候比较有效，在GPU和CRAY平台上，线程比较多的时候不work。so，本文，present different approaches for these platforms that are more highly parallelized。

## 主要内容：
1. 介绍了多核（openmp）及CRAY CMT和GPU上的并行算法。其中，多核是一种并行算法，后两个平台采用一种并行算法套路。

多核下的kmeans++初始化算法如下：\\

![](/images/paper/algo-1-kmeans++.png)

CRAY CMT的kmeans++初始化算法如下：\\

![](/images/paper/algo-2-kmeans++.png)

GPU的kmeans++初始化算法如下：\\

![](/images/paper/algo-3-kmeans++.png)


2.针对不同的n，m，k，以及测试出来的运行时间，在各个平台上，建立线性回归模型，学习参数。这样就可以预测任意一个数据规模下，在各个平台上的运行时间。并对预测的正确率进行了评估。（平方根误差）

3.建立了一个可视化工具： kmvis。可视化的目的是：indicate which platform would compute the k-means++ initialization the quickest given a particular input size of n and m, and number of clusters k.
这个工具也可以用于其他算法，在不同平台上的表现对比（升华）。
这个工具其实就是类似于matplot的画图的工具。它画出的图，横轴代表m，纵轴代表n，然后k是单独的，一个固定的k，一个图。然后在某个坐标规模下，哪个平台上运行的最快，就涂上相应平台的颜色。画出的图如下：
![](/images/paper/1-kmeans++.png)
得出的结论有：

（1）某些大规模数据，有的平台由于内存不够，没有测试结果，但是发现，相应的最好的预测结果也不发生在那个平台上，故在可视化工具中并没有处理这种缺失值的情况。

（2）One of the interesting discoveries of our performance comparison was that every single platform had a range of values for n, m, and k in which it predicted to be the fastest of all our tested platforms.

## 性能结果
1.测试了多核、cray平台上的可拓展性（随核数变化，运行时间的变化表）。

2.测试了gpu平台上，让gpu的性能与多核中的单线程版本比较。测试加速比。

3.绘制了可视化结果。分析，某个规模下，哪个平台运行的时间最短。


## 结论：
1. 同一个平台下，开启不同的线程数时，并不一定线程数越多越好； 同时，也不一定线程数等于物理线程数时最好。有时候线程数少的时候，数据局部性，各种资源的利用情况会更好。

2.当D小的时候，GPU效果最好； 当D大的时候，XMT效果最好； 当N很大的时候，XMT效果最好（其他的，有的，装不到内存中了）
当n，k很小时，多核效果很好。

3.虽然本文的优化效果不一定是最优的，但是把一个具有天然串行性的算法在各个平台上并行化啦。是具有启发性的。

## 未来的工作
1. 本文做实验选取的数据，都是n，m很大，k在[2,10]范围内的，这是受之前别人的聚类工作的影响而设置的。
未来，我们将会研究k的变化对不同平台的影响。（扩大k的变化范围。）

2.对于线性回归模型，是否可以减少参数？可否找出一个更好的另一种形式的regression analysis might provide more accurate results than linear leastsquares？当n，m，和k都在各个范围上变动时，是否会产生不一样的可视化结果，比如图中不会又一片一片的这种现象（某段规模下在一个平台上效果最佳，而是在一个点和另一个点的性能最佳都是在不同的平台上取得的）。

3.可以和related work里面的几个进行一下性能比较。



## 补充知识：

1. c++的仿函数机制。

2. gpu上的实现是使用的thrust库实现的。学习一下这个NVIDIA的并行库。


## 我的收获

1. 本文将统计模型用于高性能分析之中，这个点子不错。（研一上课，体系结构老师提过，现在做出这种结合的论文不多，学习借鉴）。

2. openmp的并行化那个算法很值得学习，证明部分我还没有看。GPU平行的思路感觉不是最优的，有很大的提升空间。

3. 本文测试时，维度比较大时，好像讲的不是很清晰，搪塞带过啦。



