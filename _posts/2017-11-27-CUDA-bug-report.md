---
layout: post
title:  CUDA优化过程中的bug记录
keywords: CUDA
categories : [CUDA]
tags : [CUDA编程]
---

记录下编程过程中遇到的bug，积累多了之后，进行归类。

## 方法论

### 分享别人的一篇关于cuda调试bug的方法总结：

http://blog.csdn.net/litdaguang/article/details/50462325


## 常见bug和解决方案整理


本部分整理自《CUDA并行程序设计 GPU编程指南》

1.cudaDevideSynchronize()函数用于同步，一个API调用完成后，使用此函数，使得该API结束后才执行下面的程序。

2.线程块的大小，计算时：

	int num_blocks = (num_elements + num_threads - 1)/num_threads; //需要向上取整。

然后在内核函数中，为了防止数组被越界访问，需要加上一个判断：

	if(tid < num_element){
		...
	}

3.host上的内存指针，和设备上的内存指针，要分清楚，malloc和free，及函数调用时，都不要写错了的。

4.




### gpu-gdb的使用：

http://blog.csdn.net/fishseeker/article/details/74178318



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



# magma-gemm

1.ceil（1/2） == 0，如果要想得到1，必须强制类型转换一下：ceil(1/(float)2) == 1

2.#define TEXUTRE_1D打开后，出现非法访问地址的bug：

如何改呢？？？（不知道呢，呜呜呜呜）

















