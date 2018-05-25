---
layout: post
title:  CUDA优化-thrust的使用
keywords: CUDA
categories : [CUDA]
tags : [CUDA编程]
---

thrust是一个类似于STL的高性能的并行库，提供了很多基本的gpu加速的primitive，如reduction，scan，sort等。
Thrust库是一堆头文件（在CUDA-dir/thrust/目录下），使用时不需要额外的配置。直接include相应的头文件即可。
若更新版本，直接下载最新的头文件，覆盖即可。




# 查看thrust的版本的例子：version.cpp（命名成cu文件也可以）


**code**：
```

 //目录：/home/limin/CUDATrain/thrust-exer/version
 #include <iostream>
 #include <version.h> 
 
 int main(void)
 {
 	int major = THRUST_MAJOR_VERSION;
 	int minor = THRUST_MINOR_VERSION;
  
 	std::cout << "Thrust v" << major << "." << minor << std::endl;
 	return 0;
}

```

**编译**：

g++  version.cpp  -I/soft/cuda7.5/include/thrust -o version


# Thrust的vector容器的使用:

Thrust提供了两个vector容器：host_vector 与 device_vector。顾名思义，host_vector位于主机端，device_vector位于GPU设备端。Thrust的vector容器与STL中的容器类似，是通用的容器（可以存储任何数据类型），可以动态调整大小。

**code**：
```

```


# fill、copy、sequence的用法：

copy函数可以用来拷贝主机端或者设备端的数据到另外一个vector。与STL中的类似，thrust::fill用于向一段元素赋特定值。thrust::sequence可以用来生成等差数列。

**code**：
```

```




# saxpy的实现：使用transform



# sort的实现：


# 参考文献：(非常好！！)

[csdn的一个博客-thrust的用法](http://blog.csdn.net/zerolover/article/details/44425545)






