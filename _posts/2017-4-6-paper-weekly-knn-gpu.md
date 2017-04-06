---
layout:     post
title:      paper-Billion-scale similarity search with GPUs(knn-optimizaiton-gpu-1)
keywords:   knn-optimization
category:   paper
tags:       [paper]
---

**前言：**

	这是Facebook AI实验室刚刚发出来的论文。关于knn算法在gpu上的优化。提出了一种用于 k-selection 的设计，其可以以高达理论峰值性能 55% 的速度进行运算，从而实现了比之前最佳的 GPU 方法快 8.5 倍的最近邻搜索。

**代码**：

	https://github.com/facebookresearch/faiss

## 内容：

本论文的相关参考：

	http://www.leiphone.com/news/201703/lzEITGcs5Miuh8k5.html

	http://www.mshuaren.com/t/fb-gpu/3718（有代码）

论文中使用的乘积量化方法来近似计算knn，乘积量化的参考（下面这个人的博客里有很多关于乘积量化和相关搜索技术的论文解读等）：
	
	http://blog.csdn.net/chieryu/article/details/50404920
	http://blog.csdn.net/chieryu/article/details/50347735
	http://blog.csdn.net/CHIERYU/article/category/6037777
	http://blog.csdn.net/chieryu/article/details/50488671

