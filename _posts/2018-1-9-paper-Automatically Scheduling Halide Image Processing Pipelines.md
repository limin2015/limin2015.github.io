---
layout:     post
title:      paper-Automatically Scheduling Halide Image Processing Pipelines
keywords:   paper-halide2016
category:   [paper]
tags:       [paper]
---

## 出处：
2016年，《Acm Transactions on Graphics》（ccf-a）


## 要解决的问题：

1.halide语言成为一个有效的产生高性能的图像处理代码的系统。他的工作方式是这样的：程序员提供如何并行的策略，即schedule，然后halide将schedule自动的实现到具体的硬件平台上。这种方法存在一个问题：程序员需要对hpc非常了解，而且schedule的生成其实是最critical的步骤。


## 摘要：

为了解决上面提到的问题，使得普通程序员也能够利用halide生成高效的代码，本文提出了一个自动产生高性能的schedule的算法。


## 前人工作

TODO


## 主要内容：

### halide简介

**主要思想**：将schedule和自动生成硬件相关的代码进行分离。（这个思想也被tvm使用。）

**Halide’s scheduling primitives**：

 compute_at：

 reorder：

 tile：




### 正式介绍算法前的例子：（通过特定的程序，看看如何生成schedule）

//补：把paper中的截图，粘过来。


1. Scheduling for Producer-Consumer Locality

**疑问**：
（1）Producer-Consumer Locality是什么？

为了计算out，一般都会需要计算一些中间结果（比如一个数组，mid-buffer）；
如果先把mid-buffer全部计算出来，再计算out，那么Producer-Consumer Locality就会比较低，大部分情况下，会导致memory-bound。


策略：

(1)一种是：为了提高并行度，先计算中间结果数组，再计算最终的结果out数组。

（2）一种是：最大化p-c-locality，以计算out为准，没产生一个out的元素之前，把它需要的中间结果的值计算出来。但是这样通过会带来冗余计算。

（3）一种是：前两者的折中。在最内层分块（这种策略叫overlapped tiling），计算一块的中间数组，然后接着计算此块的out。




2. Scheduling for Input Reuse

**疑问**：
（1）Input Reuse 是什么？

这个考虑的其实是一个函数中，对于输入数据的重用（我平常接触的都是这种），比如GEMM。input的reuse对于稠密线性代数函数和卷积的计算特别关键。（其实就是对于计算占有的函数的优化很关键）。



3. Function Bounds Analysis

（1）Function Bounds是什么：

the compiler must be able to determine the appropriate loop bounds and intermediate buffer sizes

**举例**来说，
编译器根据输入的expression来分析函数的bound，比如：
当out 数组的界属于：(xmin..xmax,ymin..ymax) 时（逗号前时x的范围，逗号后时y的范围），输入数组和中间数组的界是：
blurx: (xmin..xmax, ymin-1..ymax+1) in:
(xmin-1..xmax+1, ymin-1..ymax+1)


（2）那么如何确定函数的bound呢：

Starting from the output function, bounds inference propagates up the function dependency chain, ascribing bounds to all functions in the program DAG.

TODO: 底下这段没有看明白！！

When the Halide compiler cannot infer tight bounds for a function (e.g., due to data-dependent access by a con- sumer), the programmer can explicitly provide bounds to assist the compiler in generating efficient code (e.g., the programmer may have static knowledge that all accesses to a lookup table will be in the range 0..8)



### 本文的算法

#### 1. Function Preprocessing


#### 2. Function Grouping and Tiling：（重点）

#### 3. Function Inlining：

#### 4. Final Schedule Generation：


