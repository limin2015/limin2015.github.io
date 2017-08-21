---
layout: post
title:  paper reading-远程监督关系抽取-1(Neural Relation Extraction with Selective Attention over Instances)
keywords: 远程监督方法进行关系抽取
categories : NLP
tags:
  - paper
---

对远程监督关系抽取的几篇论文的总结，本文是第一篇:ACL-2016, 清华刘知远团队

源码：https://github.com/thunlp/NRE

## 摘要

1.存在的问题：

远程监督方法是挖掘实体关系广泛使用的一种方法，但是它存在着打错标签的问题。

2.propose a sentence-level attention-based model for relation extraction.(提出了句子级别的attention机制)

3.In this model, we employ convolutional neural networks to embed the semantics of sentences. Afterwards, we build sentence-level attention over multiple instances.(这里的instance代表一个包含已知的2个实体的句子)

## introduction

1.为什么要进行关系抽取（RE）？

知识库里面存储的关系是有限的，为了丰富知识库，如果自动的发现一些关系事实成为一个研究课题。

2.关系抽取任务的相关工作

有监督的学习方法，需要人工标记一些带有特定关系的训练数据。存在着一定的效率问题。

为此，Mintz et al., 2009 提出了使用远程监督的方法（自动给训练数据打标签），automatically generate training data via aligning KBs and texts。 他们提出一个重要假设：如果知识库中，2个实体存在某种关系，那么假设所有包含这2个实体的句子都表达了这种关系。
但是，这种假设存着一些问题：把一些句子打错了标签。（有些句子，虽然同是含有这2个实体，但是并没有表达类似的关系）

为此，(Riedel et al., 2010; Hoffmann et al., 2011; Surdeanu et al., 2012) 提出了 multi-instance learning的方法，但是他们仍然采用传统的手工提取特征的方法（eg：POS tagging），容易导致误差的累积。

(Socher et al., 2012; Zeng et al., 2014; dos Santos et al., 2015)开始使用神经网络来进行关系分类任务（不用人工提取特征啦！！）。这些方法，基于句子级别的标记数据来建立自己的分类器，从而不能应用于大规模的知识库（标记数据木有啊啊啊）

(Zeng et al., 2015) incorporates multi-instance learning with neural network model：将远程监督获得的训练数据作为神经网络的输入，进行关系抽取。但是它的方法仍然存在着一定的问题：
它假设包含这2个实体的所有句子中，至少有一个句子会表达的是这种关系，并且它只取了最有可能代表这种关系的句子作为训练数据和预测数据。这种取法可能会带来一定的信息缺失。

3.本文propose a sentence-level attention-based convolutional neural network (CNN) for distant supervised relation extraction。如下图所示：
![](/images/NLP/RE-1.png)

本文的贡献如下：
（1）与以往的神经网络关系抽取模型相比，本文利用了包含实体对的所有的句子信息。

（2）提出了attention机制，去解决远程监督的wrong label的问题。

（3）attention机制对于2中关系抽取的神经网络模型都是管用的：CNN, PCNN。


## 方法介绍

### Sentence Encoder
对包含某对实体对的句子，使用词向量的方式，表示成向量。
![](/images/NLP/RE-2.png)

过程：

1. 把一句话中的每一个字，用word2vec中的向量表示出来；把每个字距离2个实体的距离作为位置信息加入到刚刚的向量的末尾2位上。这样，每个字都有一个短向量表示；

2.对上面的短向量进行Convolution, Max-pooling and Non-linear Layers的操作，生成最后的整个句子的表示。
这个过程相当于提取每个句子的特征。

我的疑问：为什么这样设计，可以提取出特征啊？？




### Selective Attention over Instances
对包含某对实体对的所有句子，采用attention机制进行选择，将最能表达这种关系的句子们挑选出来。


## 实验



## 总结与展望



## 学到的知识

1.知识库有哪些？

Freebase，DBpedia and YAGO。这些知识库一般用3元组来表示关系。

2.关系抽取（RE）是什么？

the process of generating relational data from plain text

## 引用

[1]paperweekly对于远程监督关系抽取的论文总结：
http://mp.weixin.qq.com/s/ViQqeER1NXtJOtnLg76TWg

[2]



## 疑问

1.为什么CNN可以提取特征？想明白。
因为训练数据是有局部特征的，


## 补充
1.CNN最成功的应用是CV， 为什么NLP和speech的很多问题也可以用CNN做出来？他们的相似性在哪里？
CNN通过什么手段抓住了这个共性？为什么很多做人脸的paper会最后加入一个local connected conv?（取自wang naiyan）

查看知乎收藏。



    