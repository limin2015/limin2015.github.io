---
layout: post
title:  python学习-3
keywords: python语言
categories : [codingLanguage]
tags : [python]
---


11.遍历的几种方式：

（1）for循环：
	
  for x in words:

  for i in range(9):

  for line in open(integers.txt):


 (2)while true:   or while x>9:


 (3）if语句：

 if a and b:

 (4)



12.指针相关：

（1）
code：
	def p(L, val):
		L.append(val)
	def m(L):
		return L.pop()
	L1 = list(range(0, 20, 5))
	L2 = L1
	L3 = L2[:]
	p(L2, 20)
	p(L3, 25)
	print(L2)
	print(m(L2))
	print(L1)
	print(L3)

output：
	[0, 5, 10, 15, 20]
	20
	[0, 5, 10, 15]
	[0, 5, 10, 15, 25]

解释：



（2）


13. Python2和python3的不同：

（1）python3的print需要加括号。

（2）




14.python掉用c++：



15.numpy的histgram的使用：

https://www.programcreek.com/python/example/5991/numpy.histogram

