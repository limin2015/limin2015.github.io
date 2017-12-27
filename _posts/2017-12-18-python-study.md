---
layout: post
title:  python学习-1
keywords: python语言
categories : [codingLanguage]
tags : [python]
---



1.list相关：

list: []

list.pop() //将list的第一个元素弹出来。
list.append() //添加某个元素
list.extend()  //合并两个list

L[-1]:list中倒数第一个元素。


list可以强制类型转换为set，这样就可以去掉重复元素；

字符串可以强制转化为list：

	S = "face12"
	L = list(S)
	print ("L= ", L)
	output:
	['f', 'a', 'c', 'e', '1', '2']
<!-- T = ','.join(list(S)) -->

**list comprehension**:

[(atan2(pt[1], pt[0])*180/pi, (pt[0]**2+pt[1]**2)**0.5) for pt in points]

[word for word in words if ue in word]




2.字典：

(1)结果为什么是哪样？字典类型如何取key和value？
\\
![](/images/codingLanguage/python-dic-1.png)

（2）



3.集合：



4.（doctest）模块：
Python内置的“文档测试”（doctest）模块可以直接提取注释中的代码并执行测试。doctest严格按照Python交互式命令行的输入和输出来判断测试结果是否正确。



5.str相关的：

（1）str.count('a'):数字符串str中字符a的个数

	s = "aardvark"
	t = (v, b)
	s.count(t[0]) > s.count(t[1])

（2）

**join()**：
	
eg-1:

	str = "-";
	seq = ("a", "b", "c"); # 字符串序列
	print str.join( seq );

	output:
	a-b-c



**strip()**: 
去除两边的

**split()**:

s = str.replace(old_value, new_value).

eg:
	
	str = "this is string example....wow!!! this is really string";
	print str.replace("is", "was");//全部都换。
	print str.replace("is", "was", 3);//从头开始换，值换3个。

	output:
	thwas was string example....wow!!! thwas was really string
	thwas was string example....wow!!! thwas is really string



str.lower(): 将字符串转换成小写字母。



range():

range(a, b, step)  ==>> (a, b)，步长为1.不包括b，包含a。

for i in range(6)  ## i 是(0,5)吗？是的。



6.print

(1)format：

{：d}或者{0:d}表示c语言的%d，输出整数。

如下：

print("You need ==> 25 cent: {:d}\t10 cent: {:d}\t 5 cent: {:d}\t1 cent: {:d}".format(t25,t10,t5,t1))


(2)
\\
![](/images/codingLanguage/python-print-1.png)


(3)如何让 print 不换行?

在Python中总是默认换行的.如下：

	 CODE:
	 for x in range(0,4):  
    	print(x)  

     OUTPUT:
     0
     1
     2
     3

如果想要不换行，之前的 2.x 版本可以这样 print x, 在末尾加上 ,
但在 3.x 中这样不起任何作用。
要想换行你应该写成：

	
	for x in range(0,10):  
    	print (x,end = '')


（3）print ()

相当于打印一个换行符。

（4）

7.input()和raw_input()

raw_input将输入存成字符串；input存成数值类型。
python3只有input();


