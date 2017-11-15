---
layout: post
title:  caffe源码阅读
keywords: caffe
categories : [deep-learning]
tags : [deep-learning]
---

## 路线图

http://blog.csdn.net/kkk584520/article/details/41681085
http://blog.csdn.net/seven_first?viewmode=contents


【路线图】

（1）Caffe源码阅读路线图应该是从CAFFE_ROOT/src/caffe/proto/caffe.proto开始，了解各类数据结构，主要是内存对象和序列化磁盘文件的一一对应关系，知道如何从磁盘Load一个对象到内存，以及如何将内存对象Save到磁盘，中间的过程实现都是由Protobuf自动完成的。

**注**：没有看懂啊： 继续查！！！！


（2）第二步就是看头文件，不用急于去看cpp文件，先理解整个框架。Caffe中类数目众多，但脉络十分清晰。在Testing时，最外层的类是Caffe::Net，包含了多个Caffe::Layer对象，而Layer对象派生出神经网络多种不同层的类（DataLayer, ConvolutionLayer, InnerProductionLayer, AccurancyLayer等），每层会有相应的输入输出（Blob对象）以及层的参数（可选，Blob对象）；Blob中包括了SyncedMemory对象，统一了CPU和GPU存储器。自顶向下去看这些类，结合理论知识很容易掌握使用方法。

（3）第三步就是有针对性地去看cpp和cu文件了。一般而言，Caffe框架不需要修改，只需要增加新的层实现即可。例如你想自己实现卷积层，只需从ConvolutionLayer派生一个新类MyConvolutionLayer，然后将几个虚函数改成自己的实现即可。所以这一阶段关注点在算法上，而不是源码本身。

（4）第四步就很自由了，可以编写各类工具，集成到Caffe内部。在CAFFE_ROOT/tools/下面有很多实用工具，可以根据需要修改。例如从训练好的模型中抽取参数进行可视化可以用Python结合matplot实现。

（5）接下来，如果想更深层次学习，最好是自己重新写一遍Caffe（时间充裕的情况）。跳出现有的框架，重新构建自己的框架，通过对比就能学到更多内容。



## math_funtion 分析

http://blog.csdn.net/seven_first/article/details/47378697


## blob分析
http://blog.csdn.net/seven_first/article/details/47398613

## layer 分析

http://blog.csdn.net/seven_first/article/details/47418887

## 卷积层
http://blog.csdn.net/seven_first/article/details/47665741
http://blog.csdn.net/seven_first/article/details/47665817

还没真正看懂：TODO






## image2col如何实现的

## pooling层
http://blog.csdn.net/seven_first/article/details/47702403



## Serialization：序列化是什么？


## C++的一些特性，功能

### C++模板类使用，模板类的实例化
eg：
INSTANTIATE_CLASS(BaseConvolutionLayer);

### 智能指针
shared_ptr<>

**什么时候使用**:


**如何使用**：


### static_cast


### 仿函数

**是什么**： 

仿函数(functor)，就是使一个类的使用看上去像一个函数。其实现就是类中实现一个operator()，这个类就有了类似函数的行为，就是一个仿函数类了。

**什么时候使用访函数**：

有些功能的的代码，会在不同的成员函数中用到，想复用这些代码。


**用法**：

我怎么感觉像是回调函数呢？？（哈哈哈）

http://blog.csdn.net/tianshuai1111/article/details/7687983
http://blog.csdn.net/yzhang6_10/article/details/51297424

下面的博客写的不错：（函数指针和访函数的区别）

http://blog.csdn.net/chenhaobright/article/details/17840793

这两者有什么区别，既然有了函数指针， 还要函数对象干嘛。
首先，一个类，是数据以及对数据操作的行为的集合，但是在函数指针，是无法保存数据的， 所以，函数对象比函数指针功能更强， 因为它可以保存数据，
利用这一特性， 是函数指针无法比拟的优势。


### algorithm标准函数库里面的函数

##  










