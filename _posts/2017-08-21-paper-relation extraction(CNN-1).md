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

TODO
分为** 步：

### 1.Word Representation：

将输入的句子中的每一个word token使用向量表示（word2vec）。

### 2.提取Lexical Level Features：

传统的lexical level features primarily include the nouns themselves, the types of the pairs of nominals and word sequences between the entities.

而本文是这样选择的：We select the word embeddings of marked nouns and the context tokens.（词向量的表示）
![](/images/NLP/CNN-4.png)

### 3.提取Sentence Level Features：

问： 上面已经提取出了每个word的向量表示，为什么还要提取句子的向量表示呢？

答：single word vector models are severely limited because they do not capture long distance features and semantic compositionality, the important quality of natural language that allows humans to understand the meanings
of a longer expression.

为此，本文提出了一个最大池化的CNN去提取句子级别的表示，能够自动获取句子级别的特征。分为以下几步：
![](/images/NLP/CNN-5.png)

#### 3.1 Word Features

WF的构造过程如下：以下面这句话为例，

![](/images/NLP/CNN-6.png)
当前每个word的word embedding为xi， when we take w = 3, the WF of the third word “moving”
in the sentence S is expressed as [x2, x3, x4]. Similarly, considering the whole sentence, the WF can be
represented as follows:{[xs, x0, x1], [x0, x1, x2], · · · , [x5, x6, xe]}5

疑问：这个地方是把向量拼接起来吗？还是做累加和啊？（是前者）

note：这个过程可以捕捉到单词的上下文信息。

#### 3.2 Position Features

把每个单词距离2个实体的距离，组成一个2维的向量作为PF。

通过3.1和3.2， Combining the WF and PF, the word is represented as [WF, PF]T。这个是卷积的输入。

#### 3.3 Convolution

3.1， 3.2得到的word表示，只是每个句子中的每个word的局部特征。而我们的目的是要对一整句话打一个标签，判断它属于哪一个类。所以，我们需要merge这些特征。本文使用CNN进行这个操作。


  	Z = W1X  （1）
  	mi = max Z(i, ·) 0 ≤ i ≤ n1 （2）
  	g = tanh(W2m)    （3）
  	f = [l, g]      （4）
  	o = W3f         （5）//softmax分类器

具体计算过程的模拟，如下图所示：

![](/images/NLP/CNN-7.jpg)

![](/images/NLP/CNN-8.jpg)



### 4.输出结果：

输出结果是一个n维的向量，n代表总的关系类别数，每一维度的值代表当前句子属于此类的置信度值。


### 5.Backpropagation Training

![](/images/NLP/CNN-9.png)


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



    