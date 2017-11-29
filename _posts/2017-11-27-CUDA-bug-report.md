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

1. 现象描述：结果中前几个正确，后面的不对。然后在device里面打印了输入的数组，发现，不对的结果对应的输入也不对。

解决：host2device传数传错了！！
应该为：
err = cudaMemcpy(d_x, x, N*sizeof(DATATYPE), cudaMemcpyHostToDevice);
我写成了：
err = cudaMemcpy(d_x, x, N, cudaMemcpyHostToDevice);

2.性能没有调优：模仿magma中的进行调优。（感觉这个没啥好优化的）


## gemv

1. 现象： gemv的结果不对，不对的总是与正确结果差1. 有点规模是对的，有的规模不对。

（1）访问矩阵A时的地址算错了的：

（2）



2. 现象：GPU计算出来的值，跟CPU计算出来的值，差的不大（有的从小数点后第5位开始不一样），那么比较两个单精浮点数是否相同时，如何设置阈值呢？

（1）解决1： 需要搞清楚，到底该如何比较？跟哪些东西有关系？TODO

（2）解决2：使用sample中，matrixMulcublas里面的判断方法，相对norm值是否小于eps。（PASS）

相关函数的目录：/home/limin/CUDATrain/samples/common/inc/helper_image.h中的sdkCompareL2fe（）函数。


3. 现象：性能不好，比cublas差2-3倍，看看magma中都是使用的什么优化方法，深度调优；




#  gem2v的融合函数：

思考：share-memory的利用要减半，还OK吗？应该够用的。（吧gemv调到最优之后，把这个kernel写好）















