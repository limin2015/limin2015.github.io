---
layout: post
title:  paper reading-Yinyang K-Means,A Drop-In Replacement of the Classic K-Means with Consistent Speedup
keywords: k-means
categories : paper
tags:
  - paper
---

2015, ICML, yufen ding

## introduction

关于加速k-means的研究，有这么几类：

  1. Some try to come up with better initial centers (e.g., K-means++ (Arthur & Vassilvitskii, 2007; Bahmani et al., 2012)). （可以减少迭代次数）
  2. parallel implementations. （并行的角度研究）
  3. A complementary approach is to speed up the algorithm itself。本文关注的是这一条。


对于本文关注的对于算法本身的研究来说，For an alternative algorithm to get widely accepted, we believe that it needs to meet several requirements: 

  1. It must **inherit the level of trust** that Lloyd’s algorithm has attained through the many decades of practical use; 
  2. it must produce significant **speedups** consistently; 
  3. it must be **simple to develop and deploy**.


对于算法本身的研究，有：近似算法，KD-tree–based methods和triangular inequality–based methods：
然而，

  1. 近似算法不能保证计算的结果与原始的Lloyd’s algorithm相同。不满足第一条。
  2. **KD-tree–based methods** (Pelleg & Moore, 1999; Kanungo et al., 2002) for instance does not work well when the number of dimensions is greater than 20 (Kanungo et al., 2002)
  3. **the prior triangular inequality–based methods** (Elkan, 2003; Drake&Hamerly, 2012; Hamerly, 2010) either does not scale with the num- ber of clusters or performs poorly in some scenarios


## 摘要：

本文提出了一个基于三角不等式来减少距离计算的k-means算法。


## 算法描述

**主要思想**：

  1. 在不同的迭代步之间，使用一种过滤方法，使得可以快速判断出x这个数据点是否需要移动中心点，若不需要，这样就免去了x与所有中心点的距离计算。过滤方法：
  
    基于上界下界的判断公式：若x到当前中心点的距离的上界 <= x到其他中心点的距离的下界，那么不需要移动x的中心点）。具体的x到当前中心点的距离的上界（见下面的公式的右侧）， x到其他中心点的距离的下界（见下面的公式的左侧），如何得到。

 2. 公式：

   符号说明：

  ![](/images/paper/yinyang-1.PNG)

  计算公式：

  ![](/images/paper/yinyang-lemma.PNG)
  
  公式的证明：

  ![](/images/paper/yinyang-proof-1.PNG)
  ![](/images/paper/yinyang-proof-2.PNG)



  3. 上面的公式有一个缺点：公式的左边的下界有一个max，也就是说，只要有一个中心点的移动很大，那么就会使得公式左边的值很小，从而使得上面的公式不成立（下界不大于上界了！！，称为过滤不掉），不能过滤到很多的距离计算了。

**算法改进**：

为了改进上面的缺点，提出了GROUP FILTERING的方法。

改进思想：

  1. 因为上面的公式的左边如果使用的是全部中心点（除数据点x上一迭代所属的中心点外）的max，所以容易导致这个max很大，使得大部分的x与中心点的计算都过滤不掉，那么我把全部的中心点分为好几个组，使用每一个组的max，若一个组的max的值不算大，那么就会使上面的公式的左边得到的值比较大，容易满足上述公式（叫做：过滤掉了），即这么组的中心点与数据点的距离，就不用计算了，它们肯定不是x数据点的新的样本点。（公式右边的上界的判断是不改变的，仍然使用的是上一个算法提供的值。）

  2. 若某个组的左值不满足过滤条件，那么就需要进一步的判断，也就是说这个组里的其中有一个中心点，距离x的距离要小于x的上一轮的中心点，它可能为成为x的新的中心点。如何判断呢？设计了新一轮的过滤方法：

   ![](/images/paper/yinyang-lemma2.PNG)



**更新中心点阶段的公式**：

   ![](/images/paper/yinyang-updateCenter.PNG)


## 最终的算法

  ![](/images/paper/yinyang-algo.PNG)

  ![](/images/paper/yinyang-algo-2.PNG)


## 对比

与Elkan，Drake (Drake & Hamerly, 2012) and standard K-means进行对比。

1. 首先，理论分析，与基于三角不等式的方法的对比：Elkan和Drake的工作。

 ![](/images/paper/yinyang-compare-1.PNG)

 ###Elkan的算法：

 1. 定理简介：

  **lemma-1**：
  ![](/images/paper/yinyang-elkan.PNG)

  这个lemma用于在同一个迭代内部的时候消除多余的距离计算。
  
  **lemma-1的应用是**：给出了每一个数据点到最近的中心点的一个**上界**
  ![](/images/paper/yinyang-elkan-3.PNG)

  **lemma-2**：
  ![](/images/paper/yinyang-elkan-2.PNG)
  这个lemma其实就是两边之差小于第三边。这里用来在不同迭代步之间，消除多余的距离计算。
  
  **lemma-2的应用**：给出了下一次迭代时，每一个数据点到每一个中心点的距离的一个**下界**
  ![](/images/paper/yinyang-elkan-4.PNG)




 2. 算法：
  ![](/images/paper/yinyang-elkan-algo-1.PNG)
  ![](/images/paper/yinyang-elkan-algo-2.PNG)




2. 这3中实现都是在Graphlab中实现的，都是parallel的。有源代码。

3. 它的实验分析很细致。


## 我的收获

1. 推导了这个paper中的公式，整体感觉不难，但是也不好想。
思考的方式是从：在上一轮计算结果的基础上，如何在下一轮的计算中，减少距离计算？

2. TODO:
我需要整理另外的2个基于三角不等式的算法和引用它的一个三角不等式的paper：Fast K-Means with Accurate Bounds