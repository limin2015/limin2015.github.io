---
layout: post
title:  paper reading：A Novel Top-k Selecting Algorithm
keywords: paper-top-k
categories : [paper]
tags : [top-k]
---

# DC-Top-k: A Novel Top-k Selecting Algorithm and Its Parallelization
## 出处：
2016年，ICPP（华中科大）

## 要解决的问题：
提出了一种新的求序列前k大（或小）的数的算法。（top-k问题）
本文解决的top-k问题：只需找到top-k，前k个的顺序，不要求有序。

## reference版本 ：Partial Quicksort 
比较次数： C(n,k) = 2(n+1)Hn+2n-6k+6-2(n+3-k)Hn+1-k
交换次数：C(n,k)/6
	where Hn denotes the n-th harmonic number.
## 提出的算法：
**理论分析：**

	比较次数：at most (2-1/k)n+O(klog2k) comparisons
	交换次数：O(klog2k) exchanges 
与reference相比，比较次数相当，但是交换次数减少啦；

**实验结果:** 

		1-3 times faster than Partial Quicksort；
		随着k增大, 比Min-heap based top-k algorithm更加有效；
		并行实现的scalability比partial quicksort好；


## 主要内容：
## related work：（解决top-k问题的算法整理）

### Tournament Sort [6]：

### heap sort：（上课学过）
worst-case O(n)+O(klog2n) runtime

### 最近提出的一个基于Min-heap的算法[3,7]：
O(nlog2k) runtime。 当k很大的时候，效率大大降低；

### 基于 Quicksort和其变种的算法：
例如：Partial Quicksort [8], Incremental Quicksort [9,10])
复杂度：O(n)
与普通快排的区别：只对包含top-k元素的组进行递归。


### 本文的DC-Top-k算法
The basic idea: 

 - Suppose the input array consist of n elements. Divide r[0..n-1] into k groups and select the local maximum in each group, i.e., divide the top-k problem to k top-1 problems.
 - Then we get k local maximums. From a probabilistic perspective, k local maximums partly overlap with k global maximums. We set the minimum in the local maximums as the threshold. 
 - Finally, we select top-k from the valid elements。 
算法描述：
	 
算法解释：


## 实验
### 配置：
**输入数据为：**

**测试标准：** 
**测试规模：**

	
**测试项目：**

					
### 结果：  




