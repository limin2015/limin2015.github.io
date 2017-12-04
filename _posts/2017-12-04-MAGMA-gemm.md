---
layout: post
title:  CUDA性能优化-MAGMA-GEMV-GEMM-Implementation
keywords: CUDA
categories : [CUDA]
tags : [CUDA编程]
---

介绍magma库中的gemv和gemm的实现。参考magma的源代码，和相应的论文


# magma-gemv

把我的结果也粘过来：



# magma-symv：暂时不整理这个算法的优化

TODO



# magma-gemm


## feimi架构之前的GTX280上的GEMM

我的感觉：将matrix 映射到线程上，两层分块。（跟在sw上的设计思路是一样的！！）

![](/images/cuda/gemm-1.png)
![](/images/cuda/gemm-2.png)



## GEMM on feimi:

我的感觉是：因为feimi架构的访问register比访问shmem快，在之前的基础上，加了一层寄存器分块。

![](/images/cuda/gemm-3.png)
![](/images/cuda/gemm-4.png)
![](/images/cuda/gemm-5.png)
![](/images/cuda/gemm-6.png)

我需要画一个图，来表示，最内层分块是如何进行的（就像在sw上一样的）：



# reference

[Optimizing symvon GPUs-2011](http://www.netlib.org/utk/people/JD/JackDongarra/PAPERS/Optimizing-Symmetric-Dense-Matrix-Vector-Multiplication-on-GPUs.pdf)

[Optimizing Memory-Bound Numerical Kernels on GPU Hardware Accelerators-2012](http://www.icl.utk.edu/files/publications/2012/icl-utk-530-2012.pdf)

[An Improved MAGMA GEMM for Fermi GPUs](http://www.netlib.org/lapack/lawnspdf/lawn227)







