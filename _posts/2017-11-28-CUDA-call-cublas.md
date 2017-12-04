---
layout: post
title:  CUDA性能优化-调用cublas
keywords: CUDA
categories : [CUDA]
tags : [CUDA编程]
---

介绍如何调用cublas里面的函数。测试一下cublas的性能。

# 看看api:

[cublas的api的文档地址](http://docs.nvidia.com/cuda/cublas/#cublas-lt-t-gt-gemv)



# scal（blas-1级）


# gemv（blas-2级）：OK

矩阵本身是列优先的调用（修改的CUDA的samples中的matrixMulCUBLAS）：

/home/limin/CUDATrain/svm/lmblas/gemv/gemvCublas

矩阵本身是行优先的调用：（是不是必须得转置了啊？）





# gemm（blas-3级）：OK 

这个例子，在CUDA的samples有一个例子。（参考这个例子，跑起来试试）

目录：/home/limin/CUDATrain/samples/0_Simple/matrixMulCUBLAS


## 关于列优先，行优先：

cublas是按照列优先算的（为了兼容Fortran程序），如果调用者的矩阵是行优先存的，那么该如何计算呢？

解决：（例子的最上面的注释中有）行优先存储的a（m*k），b(k*n)，c(m*n)，想要计算 c = a*b，一种方法是转置，可是开销太大。
考虑到：c^t = （a*b）^t = b^t * a^t,正好相当于转置，即调用时，相当于调用b*a的矩阵乘，即可完成结果。如下：

cublasSgemm(handle, CUBLAS_OP_N, CUBLAS_OP_N, n, m, k, &alpha, d_B, n, d_A, k, &beta, d_C, n);

若本来a，b，c就是列优先存储的呢？a（m*k），b(k*n)，c(m*n)，想要计算c = a*b，如何调用：
cublasSgemm(handle, CUBLAS_OP_N, CUBLAS_OP_N, m, n, k, &alpha, d_A, m, d_B, k, &beta, d_C, m);


看看这个例子：（加深理解）

	https://www.cnblogs.com/scut-fm/p/3756242.html


## TODO: 把blas中的gemv和gemm，测试一下，整理一个图表，看看效果如何？大约可以达到多少？（心里有数）



看这个！！！

Matrix computations on the GPU CUBLAS and MAGMA by example



