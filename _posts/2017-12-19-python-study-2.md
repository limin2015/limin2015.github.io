---
layout: post
title:  python学习-2
keywords: python语言
categories : [codingLanguage]
tags : [python]
---


7.sorted和list.sort()

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


8.lamda表达是：

lambda函数就是个临时函数，有点像C语言的宏定义或者C++里面的inline，参数必须只能是传值。

冒号前面相当于函数参数，后面相当于返回值。

L.sort(key=lambda x: x[1])

L.sort(key=lambda x: [x[1],x[0]])


9.几个高级函数：

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


eg-3：

\\
![](/images/codingLanguage/python-map-1.png)

eg-4：

\\
![](/images/codingLanguage/python-map-2.png)




**reduce()**:

reduce把一个函数作用在一个序列[x1, x2, x3...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算，其效果就是：
reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)

eg-1:

	def fn(x, y):
		return x * 10 + y

	reduce(fn, [1, 3, 5, 7, 9])
	
	output:
	13579

10.文件读取：


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

第三题：

f_1 = open("elems.txt","w")
f_2 = open("birches.txt","w")
for line in open("trees.txt"):
	if 'elm' in line.lower() and 'birch' in line.lower():
    	continue
    if not 'elm' in line.lower() and not 'birch' in line.lower():
        continue
    if 'elm' in line.lower():
        f_1.write(line)
    if 'birch' in line.lower():
        f_2.write(line)
f_1.close()
f_2.close()


第九题：先写上一个结果：

True

第4题：
def highest_peak(L):
	p_l = []
	for i in range(1, (len(L)-1)):
 		if (L[i])>(L[i-1]) and (L[i]>L[i+1]):
  			p_l.append(L[i])
 	if not len(p_l):
 		return -1
  	p_l.sort()
 	return p_l[-1]