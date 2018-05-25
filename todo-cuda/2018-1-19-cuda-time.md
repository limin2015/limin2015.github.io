---
layout: post
title:  CUDA性能优化-计时
keywords: CUDA
categories : [CUDA]
tags : [CUDA编程]
---


介绍如何在host端和kernel端对cuda 程序进行计时。

## 计时工具

1. 在host端的计时工具：

	eg：示例代码
	cudaEvent_t start, stop;
	float elapsedTime;

	cudaEventCreate(&start);
	cudaEventRecord(start,0);

	//Do kernel activity here

	cudaEventCreate(&stop);
	cudaEventRecord(stop,0);
	cudaEventSynchronize(stop);

	cudaEventElapsedTime(&elapsedTime, start,stop);
	printf("Elapsed time : %f ms\n" ,elapsedTime);

注意：Elapsed time即为kernel的执行时间，单位为**ms**。



2. kernel端的计时：


（1） 使用clock_t clock(); 或者long long int clock64(); 
[nvidia-doc](http://docs.nvidia.com/cuda/cuda-c-programming-guide/index.html#time-function)
这两个函数，可以获得kernel内部的某一段代码的clock数目，每个线程都会得到一个值，即每个线程在执行代码用了多少个时钟周期。
必须除以GPU的频率才能得到时间。

	//eg: 示例代码
	
	__global__ void magic(float *mean, int *myclock){
		int i, tid = threadIdx.x + blockIdx.x * blockDim.x;
		float t, sum=0.0;
		clock_t start = clock();
		if ( tid < dimy )
		{
			for(i=0;i<dimx; i++){
				t = tex2D( input, i, tid );
				sum = sum + t*t;
			}
			clock_t stop = clock();
			myclock[tid] = (int)(stop-start);
		}
	}

note: 上面的示例代码，引自：[ref](https://stackoverflow.com/questions/15109874/using-clock-function-in-cuda?rq=1)


（2）clock函数得到的是cycle数，如何换算成时间呢？

必须除以GPU的频率（每s多少个时钟周期）才能得到时间。


	int get_GPU_Rate()

	{

	cudaDeviceProp deviceProp;//CUDA定义的存储GPU属性的结构体
	cudaGetDeviceProperties(&deviceProp,0);//CUDA定义函数
	return deviceProp.clockRate;

	}

若频率是KHZ， 则得到的时间为ms，
that is Divide it by the shader clock frequency in kilohertz to get an answer in milliseconds

注意：

1. NVIDIA_CUDA-8.0_Samples/1_Utilities/deviceQuery中的GPU Max Clock rate这项的结果即为gpu的时钟频率。

2. 我发现samples中的程序**deviceQuery.cpp**中的单位换算是不对的：

程序如下：
printf(" GPU Max Clock rate: %.0f MHz (%0.2f GHz)\n", deviceProp.clockRate * 1e-3f, deviceProp.clockRate * 1e-6f);

deviceProp.clockRate得到的是HZ，如果想转化为MHZ，得乘以1e-6f吧，因为中间还有一个KHZ。
