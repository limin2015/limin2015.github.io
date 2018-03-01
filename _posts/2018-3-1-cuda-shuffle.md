---
layout: post
title:  CUDA性能优化-shuffle指令
keywords: CUDA
categories : [CUDA]
tags : [CUDA编程]
---

整理一下用到的shuffle指令。

**shuffle指令功能：**

shuffle指令，允许thread直接读其他thread的寄存器值，前提是两个thread在 同一个warp中。


# __shfl

下面的两个blog中的例子不错：

https://www.cnblogs.com/1024incn/p/4706215.html

http://blog.csdn.net/lingerlanlan/article/details/25401565


int __shfl(int var, int srcLane, int width=warpSize);

int __shfl_up(int var, unsigned int delta, int width=warpSize)

int __shfl_down(int var, unsigned int delta, int width=warpSize)

int __shfl_xor(int var, int laneMask, int width=warpSize)






# ref

https://www.cnblogs.com/1024incn/p/4706215.html

http://blog.csdn.net/lingerlanlan/article/details/25401565