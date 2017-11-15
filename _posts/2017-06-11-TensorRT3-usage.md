---
layout: post
title:  TensorRT3-usage
keywords: TensorRT推理框架
categories : [CUDA]
tags : [CUDA编程]
---

TensorRT框架是NVIDIA专为推理做的一个高性能的库。不开源。自TensorRT3版本开始绑定python接口（INT8精度的没有python接口），之前的版本只支持C++调用。



# 安装

到以下网址下，下载TensorRT的安装包，（需要注册开发者账户，我的账号是qq邮箱）
![](https://developer.nvidia.com/tensorrt)
下载页面如下图所示：
![](/images/cuda/tensorrt-install.png)

按照install文档安装即可。


# 目录（tree -d）：


# 自带的例子分析：

## sample文件夹下的c++例子：

## python接口的例子（）：

使用virtualenv venv安装了python接口，故，python接口的例子在venv/bin64/Tensorrt/example/，
主要有googlenet和mnist的例子。


# 测试googlenet的TensorRT的推理性能（与caffe的推理作对比）


## 代码

## 结果

# 学习资料


