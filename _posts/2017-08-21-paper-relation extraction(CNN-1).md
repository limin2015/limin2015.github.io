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

2.相关工作

3.本文的贡献：



## 方法介绍
1.


## 实验



## 总结与展望



## 学到的知识



## 引用





## 疑问



## 补充



    