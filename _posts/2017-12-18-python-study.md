---
layout: post
title:  python学习
keywords: python语言
categories : [codingLanguage]
tags : [python]
---



1.list相关：

list: []

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



2.（doctest）模块：
Python内置的“文档测试”（doctest）模块可以直接提取注释中的代码并执行测试。doctest严格按照Python交互式命令行的输入和输出来判断测试结果是否正确。



3.str相关的：

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



4.print

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




5.input()和raw_input()

raw_input将输入存成字符串；input存成数值类型。
python3只有input();


6.sorted和list.sort()

sorted是内置函数。list.sort()是list的成员函数。


list.sort()函数的使用：

默认是升序的排序。

如果写cmp函数，使他实现不同的排序策略？（感觉我有点看晕了的！！）


(a)降序排序：

	def rev(x):
	return -x
	L = [1, 10, 3, 6]
	L.sort(key=rev)
	print(L)

	output：
	[10, 6, 3, 1]

（b）一个由字符串组成的list，按照字符串的长度排序。
\\
![](/images/codingLanguage/python-sort-1.png)

(c)将以下list排序，先按第二个元素递增，第二个元素相同的，第一个元素递增。
L = [ [11,2], [5,8], [5,2], [12,3], [1,3], [10,2], [12,1], [12,3] ]

法一：

	def return_y(x):
	return x[1]
	L = [ [11,2], [5,8], [5,2], [12,3], [1,3], [10,2], [12,1], [12,3] ]
	L.sort()
	L.sort(key=return_y)
	print(L)

法二：

	def flip_coordinates(x):
	return [x[1], x[0]]
	L = [ [11,2], [5,8], [5,2], [12,3], [1,3], [10,2], [12,1], [12,3] ]
	L.sort(key=flip_coordinates)
	print(L)

或者使用lamda表达式来表示：

法一：
	L = [ [11,2], [5,8], [5,2], [12,3], [1,3], [10,2], [12,1], [12,3] ]
	L.sort()
	L.sort(key=lambda x: x[1])
	print(L)
法二：
	L = [ [11,2], [5,8], [5,2], [12,3], [1,3], [10,2], [12,1], [12,3] ]
	L.sort(key=lambda x: [x[1],x[0]])
	print(L)


7.lamda表达是：

lambda函数就是个临时函数，有点像C语言的宏定义或者C++里面的inline，参数必须只能是传值。

冒号前面相当于函数参数，后面相当于返回值。

L.sort(key=lambda x: x[1])

L.sort(key=lambda x: [x[1],x[0]])


8.

**filter(function, list)**:

filter（function,list）返回一个新list。把list中的符合function函数的元素过滤出来。function一般用lamda表达式来表示。


**map()**:

map()函数接收两个参数，一个是函数，一个是序列，
map将传入的函数依次作用到序列的每个元素，并把结果作为新的list返回。

eg-1:

	def f(x):
		return x * x

	map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])

	output:
	[1, 4, 9, 16, 25, 36, 49, 64, 81]

eg-2:

	map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])
	
	output:
	['1', '2', '3', '4', '5', '6', '7', '8', '9']

**reduce()**:

reduce把一个函数作用在一个序列[x1, x2, x3...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算，其效果就是：
reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)

eg-1:

	def fn(x, y):
		return x * 10 + y

	reduce(fn, [1, 3, 5, 7, 9])
	
	output:
	13579

9.文件读取：


(1)
![](/images/codingLanguage/python-file-1.png)

(2)将文件中的每一行的元素倒转，然后把第1行和最后一行交换，第2行和倒数第二行交换。。。
\\
![](/images/codingLanguage/python-file-2.png)

code:

	fname = input("Enter filename => ")
	f = open(fname)
	lines = []
	for line in f:
		m = line.strip().split(",")
		line = m[1] + "," + m[0] + "\n"
		lines.append(line)
	f = open(fname,"w")

	for i in range(-1,-len(lines)-1,-1):
		f.write(lines[i])
	f.close()
	print ("File reversed!")


(3)


10.遍历的几种方式：
（1）for循环：
	
  for x in words:

  for i in range(9):

  for line in open(integers.txt):


 (2)while true:   or while x>9:


 (3）if语句：

 if a and b:

 (4)



11.指针相关：

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


12. Python2和python3的不同：

（1）python3的print需要加括号。

（2）

