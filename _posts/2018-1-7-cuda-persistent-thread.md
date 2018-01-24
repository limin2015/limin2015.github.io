---
layout:     post
title:      CUDA的persistent thread（永久线程）
keywords:   stream
category:   CUDA
tags:		[CUDA编程]
---


这个需要调研一下：很多paper中提及了的。


找个代码看看！！



# persistent thread programming style:

[A Study of Persistent Threads Style GPU Programming for GPGPU Workloads](http://xueshu.baidu.com/s?wd=paperuri%3A%287ce95fb005239e06e86c2634b147f940%29&filter=sc_long_sign&tn=SE_xueshusource_2kduw22v&sc_vurl=http%3A%2F%2Fieeexplore.ieee.org%2Fxpls%2Fabs_all.jsp%3Farnumber%3D6339596&ie=utf-8&sc_us=10768365825906481192)

思想：相当于在software层面上，实现了任务和block的绑定。

**那么有什么好处呢，多哪种workload会产生好的结果呢？？**


两步：（没大懂！！）

1. Maximal Launch: A kernel uses at most as many blocks as can be concurrently scheduled on the SM:

Since each thread remains persistent throughout the execution of a kernel, and is active across traditional block boundaries until no work remains, the program- mer schedules only as many threads as the GPU SMs can concurrently run. This represents the upper bound on the number of threads with which a kernel can launch. The lower bound can be as small as the num- ber of threads required to launch a single block. 

2. Software schedules work through work queues, not hardware:

The traditional programming environment does not expose the hardware scheduler to the programmer, thus limiting the ability to exploit workload communication patterns. In contrast, the PT style bypasses the hard- ware scheduler by relying on a work queue of all blocks that are to be processed for kernel execution to com- plete. When a block finishes, it checks the queue for more work and continues doing so until no work is left, at which point the block retires.



看一下这个paper：

https://svail.github.io/persistent_rnns/


# 引用


[persistent-thread-stack-overflow](https://stackoverflow.com/questions/14821029/persistent-threads-in-opencl-and-cuda)