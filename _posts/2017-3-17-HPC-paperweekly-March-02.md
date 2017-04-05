---
layout: post
title:  paper reading：Comparison of parallel sorting algorithms
keywords: paper-并行排序
categories : [paper]
tags : [overview]
---

## 出处：
2015年，Faculty of Computer and Information Science, University of Ljubljana, Slovenia（学校在英国排名200多名）

## 要解决的问题：
这是一篇技术报告。实现（串行和并行）并比较了以下几种排序算法：bitonic sort, multistep bitonic sort, adaptive bitonic sort, merge sort, quicksort, radix sort and sample sort。为什么要这样做？因为至今还没有人把这几种排序算法放在一种平台上进行比较。

## 主要内容：
### bitonic sorting：
优点：它的比较的序列和方向被提前决定了，与输入序列无关。
缺点：对短的序列很有效。对长序列排序时，受限于share memory的大小，变的更慢啦；长的序列需要每次都得访问global memory。这是产生了下面的多步bitonic sorting。
引用：Sorting networks and their applications（1968）

### multistep bitonic sort：
为了解决上面算法的缺点。
引用：Fast in-place, comparison-based sorting with CUDA: A study with bitonic sort（2011）

### adaptive bitonic sort：
引用：A novel sorting algorithm for many-core architectures based on adaptive bitonic sort（IPDPS 2012）

### merge sort：
引用：Designing efficient sorting algorithms for manycore GPUs（IPDPS 2009）

### quicksort：
引用：A practical quicksort algorithm for graphics processors[2010]

### radix sort：
查一下，看看串行的实现了什么功能。

### sample sort:
引用：Deterministic sample sort for GPUs[CoRR 2010]


另外一个经常用的操作：**并行规约**：看看，学学。
引用:Optimizing Parallel Reduction in CUDA[2008] （技术报告）

## 实验
### 配置：
**输入数据为：**

	均一分布，高斯分布，有序，反向有序，全部为0；
	only key； （key, value）对；

**测试标准：**  50次，取平均
**测试规模：**

		from 215 to 225 for 32-bit numbers and from 215 to 224 for 64-bit numbers； 
		length 2n + 2n-1 (for n =15, . . . , 24)（对于非规整的数）
**测试项目：**

		串行的sort ratio（每s给多少个数排序）；
		并行的sort ratio；
		并行相对串行的加速比；
				
### 结果：  

串行情况下:

	radix sort > quicksort > sample > bitonic （merge在sample与quick之间徘徊）
并行情况下：

	merge sort > IBX bitonic > quick sort
加速比：

	IBX bitonic sort > bitonic sort > merge sort > quick sort(==sample sort)