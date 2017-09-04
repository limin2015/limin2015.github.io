---
layout: post
title:  NLP-wordnet
keywords: NLP-wordnet
categories : NLP
tags:
  - NLP
---


## wordnet是什么？

Wordnet是一个词典。每个词语(word)可能有多个不同的语义，对应不同的sense。而每个不同的语义（sense）又可能对应多个词，如topic和subject在某些情况下是同义的，一个sense中的多个消除了多义性的词语叫做lemma。


## 怎么使用wordnet？

使用NLTK包进行处理：


	from nltk.corpus import wordnet as wn
	wn.synsets('motorcar')
	wn.synset('car.n.01').lemma_names




## 补充：
hypernym:上位词，
hyponym：下位词（a word that is more specific than a given word）
Synonyms：同义词
