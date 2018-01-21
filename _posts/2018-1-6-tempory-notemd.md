---
title: 1月6日的笔记（会删除）
layout: post
categories:
  - life
tags:
  - Life
  - 生活
---


# IR表示的：

知乎的这个介绍非常好：

https://www.zhihu.com/question/64091792/answer/217687988

[深度学习的IR“之争”](http://www.sohu.com/a/191605477_473283)

: 这里面的东西，还没有整理完成。


# nnvm：

http://www.dataguru.cn/article-12239-1.html


# tvm：

[tvm-document](http://docs.tvmlang.org/)


# halide:

[halide](http://halide-lang.org/)

http://graphics.cs.cmu.edu/projects/halidesched/


# tensorflow的XLA:


"XLA Overview", https://www.tensorflow.org/performance/xla/

"XLA: TensorFlow Compiled!",https://www.youtube.com/watch?v=kAOanJczHA0




[教程 | 谷歌官博详解XLA：可在保留TensorFlow灵活性的同时提升效率](http://www.sohu.com/a/128440204_465975)

XLA 使用 JIT 编译技术来分析用户在运行时（runtime）创建的 TensorFlow 图，专门用于实际运行时的维度和类型，它将多个 op 融合在一起并为它们形成高效的本地机器代码——能用于 CPU、GPU 和自定义加速器（例如谷歌的 TPU）。

 TensorFlow 如何利用 XLA、JIT、AOT 和其它编译技术来最小化执行时间并最大限度地利用计算资源。


 我的总结：
 
 1.我感觉XLA跟msra-sys实现的kf有点相似。
 2.没有详细说明技术细节：运行了JIT，AOT技术。



# 其他的系统：

Intel’s NGraph（如下图），HP的Cognitive Computing Toolkit (CCT)， IBM的SystemML


intel-nervana：

[/intel-nervana-graph](https://ai.intel.com/intel-nervana-graph-preview-release/)




# 开发工具： vscode

https://code.visualstudio.com/docs/?dv=win

https://code.visualstudio.com/docs?start=true





#  常用的编译器：

https://www.cnblogs.com/qoakzmxncb/archive/2013/04/18/3029105.html

http://blog.csdn.net/maado/article/details/51114913



gcc：

clang：

llvm：

按照下面的教程走一波：

http://llvm.org/docs/tutorial/



# c++的学习

Effective Modern C++：

https://zhuanlan.zhihu.com/p/21102748






一个搞机器学习的人的blog：

http://colah.github.io/about.html




# 1-21

1. Efficient Kernel Management on GPUs 这个paper不错。

2. The Case for GPGPU Spatial Multitasking读

3. Dynamic Resource Management for Efficient Utilization of Multitasking GPUs


4. Optimizing data warehousing applications for GPUs using dynamic stream scheduling and dispatch of fused and split kernels


5. Optimizing Memory Efficiency for Convolution Kernels on Kepler GPUs


6. maxDNN: An Efficient Convolution Kernel for Deep Learning with Maxwell GPUs

7. Kernel Fusion: An Effective Method for Better Power Efficiency on Multithreaded GPU

8. Systematic Fusion of CUDA Kernels for Iterative Sparse Linear System Solvers


9. 