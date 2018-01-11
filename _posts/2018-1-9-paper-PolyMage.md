---
layout:     post
title:      paper-PolyMage, Automatic Optimization for Image Processing Pipelines（2015）
keywords:   paper-PolyMage
category:   [paper]
tags:       [paper]                                         
---

这篇文章是halide2016里面基于的文章，halide2016很多东西是从这篇文章中学来的， 且作者都是同一个。



# 出处：
2017年，ASPLOS（ccf-a）

# 要解决的问题：

这篇文章也是在halide的基础上，做schedule的自动生成。但是他的大部分考虑都是在多核cpu上的。

domain-specific language：DSL

# 摘要：

1.Our optimization approach primarily relies on the transformation and code generation capabilities.

2.the first model-driven compiler for image processing pipelines that performs complex fusion, tiling, and storage optimization automatically.

3.比手动schedule的halide快1.81×.

4.貌似只有多核的啊！！！（verify！！）

主要贡献：

The key optimization tech- niques that we present are:

- • a method for overlapped tiling tailored for heterogeneous image processing stages,
- • a heuristic, modeling the trade-off between locality and redundant computation, for partitioning a pipeline into
groups of stages that are later fused together with over-lapping tiles,
- • storage optimization and code generation for general- purpose multicores accounting for SIMD parallelism,
- • and an autotuning mechanism for exploring a small pa- rameter space resulting from our model-driven approach.


# 前人工作

TODO


# 主要内容：


## 