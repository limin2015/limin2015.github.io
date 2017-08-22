---
layout: post
title:  paper reading-远程监督关系抽取-0(Relation Classification via Convolutional Deep Neural Network)
keywords: 远程监督方法进行关系抽取
categories : NLP
tags:
  - paper
---


对远程监督关系抽取的几篇论文的总结，本文是第一篇:ACL-2014, 作者为自动化所的zeng diaojian。是第一个使用CNN进行关系抽取的论文。


## 摘要
1.目前最好的关系抽取：先提取特征，再代入分类模型。但是这样容易产生累积误差。

2.本文使用CNN来提取lexical and sentence level features。首先将word转化为向量表示（使用词嵌入模型），然后根据给定的实体提取词汇级别的特征，同时使用CNN学习句子级别的特征表示，这2层的特征被拼接在一起，作为最终的特征表示。最后，将上面得到的特征代入到softmax分类器，来预测2个标记的实体的关系。


## introduction
1.问题定义：

given a sentence S with the annotated pairs of nominals e1 and e2, we aim
to identify the relations between e1 and e2 (Hendrickx et al., 2010).

2.动机：

关系分类最有代表性的方法是使用监督的方法：基于特征的，基于核方法的。虽然这样的方法正确率挺高，但是需要使用已有的NLP工具，容易造成误差累积，且需要人工提取特征。

3.本文提出了***（跟摘要的一样）

4.Collobert et al., 2011是第一个将CNN用于NLP任务的人。相比它的，首先，我们是首次用于关系分类任务中。其次本文特别的加了一个2对实体的距离的特征。

3.本文的贡献：

（1）A convolutional DNN is employed to extract lexical and sentence level features.（没有数据的预处理啦）

（2）position features are proposed to encode the relative distances to the target noun pairs in the CNN.

 (3)使用 SemEval-2010 Task 8 dataset进行测试，发现（2）的特征对结果很关键。同时本文取得了目前最好的结果。

## 相关工作

参考论文中。

## 方法介绍

TODO！！ 还是没有看明白！！！

1.


## 实验

三组实验：

一：如何选参，参数对结果的影响分析；
![](/images/NLP/CNN-3.png)

二，CNN提取的特征与传统方法企图的特征的效果比较；

看看传统的方法都有哪些？？
![](/images/NLP/CNN-2.png)

三：分解本文的CNN方法，不同的特征对结果的影响：（类似于控制变量法）
![](/images/NLP/CNN-1.png)

## 总结与展望

1.本文提出了使用CNN来提取lexical and sentence level features，进行关系分类的方法。position features (PF) are successfully proposed to specify the pairs of nominals to which we expect to assign relation labels（该特征的提出，有性能提升约9.2%）.本文的方法超过了所有使用NLP tool提取特征的方法。 


## 学到的知识

1.神经网络的结构为什么那样设计，每一步都有理由，解释的不错！！多看几遍！


## 引用

[Hendrickx et al., 2010]




## 疑问



## 补充



    