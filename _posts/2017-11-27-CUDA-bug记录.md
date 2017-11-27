---
layout: post
title:  CUDA优化过程中的bug记录
keywords: CUDA
categories : [CUDA]
tags : [CUDA编程]
---

记录下编程过程中遇到的bug，积累多了之后，进行归类。

## axpy

目录：/home/limin/CUDATrain/svm/lmblas/axpy （实验室的gpu服务器）

时间：2017.11.27

现象描述：结果中前几个正确，后面的不对。然后在device里面打印了输入的数组，发现，不对的结果对应的输入也不对。

解决：host2device传数传错了！！
应该为：
err = cudaMemcpy(d_x, x, N*sizeof(DATATYPE), cudaMemcpyHostToDevice);
我写成了：
err = cudaMemcpy(d_x, x, N, cudaMemcpyHostToDevice);










