---
layout: post
title:  linux命令-series-1
keywords: linux
categories : [linux]
tags : [linux，commond]
---

说来也惭愧，从大四开始接触使用Linux OS，到现在仍然是一知半解，甚至有时候连装个软件都有问题。反思了下，自己 一直贯彻着现用现查的原则，没有用心理解，整理，一些东西。要是经常用还是可以，如果不经常用，有些最基本的东西，过段时间就忘啦。忘记后，再重新查，又浪费很多时间。
经过深刻的反思，以后要养成良好的梳理，整理的习惯。把自己用过的东西以专题的形式记录下来，既受益于自己，说不定还能帮助到别人~~

## 命令大全：
http://man.linuxde.net/set

http://linuxtools-rst.readthedocs.io/zh_CN/latest/base/04_disk.html


## 我经常使用的命令

### sudo模式

	进入：sudo su
	退出：exit / logout / ctrl D

### 查找命令
http://www.cnblogs.com/sunleecn/archive/2011/11/01/2232210.html

在当前目录下查找**.file 文件。:

	find ./ -name *.file    

whereis:（比find快。和locate类似，都是从数据库查找。）
whereis命令只能定位可执行文件、源代码文件、帮助文件在文件系统中的位置。

	whereis -m svn 查出说明文档路径；
	whereis -s svn 找source源文件。
	whereis -b svn 找相关的二进制文件。

locate:查找是否存在此文件，存在时返回路径。（比find速度快一些）:

	locate *.file: 

grep:

	grep "SLAVE_FUN" *.h
	grep -irn "main.c" ./    //看代码的时候经常用。循环查找。

查看某个工具的安装的路径：

	type mpirun or type mpicc //查看mpirun的路径

which mpicc
eg：/usr/sw-mpp/mpi2/bin/mpicc(sw上，貌似这个mpicc是sw的编译器)


### 文件权限命令

1. 文件权限命令：r(4),w(2),x(1)


	sudo chmod 777 *.file  //为文件的所有用户（root，user，other）添加所有权限（读写执行）
	sudo chmod a+x  *.file //为文件的所有用户（root，user，other）添加执行权限

	相应的，r+x, u+x, o+x为分别为单个的用户添加执行权限。

2.有时候 ./build.sh 不work， 因为没有加权限。

	一种方法是加权限-》chmod a+x build.sh，然后 ./build.sh。	
	一种方法是sh build.sh。


### 服务器与本地（or服务器）间文件传输
cite: http://www.cnblogs.com/eczhou/archive/2012/09/17/2689086.html


上传当前服务器的reduction.cu到目标服务器（limin@...）上的~/dir/目录下。(不指定当地的目录不可以)：

	scp reduction.cu limin@10.12.0.199:~/dir/


### 解压缩命令：
tar：

	解压：tar zxvf FileName.tar.gz
	压缩：tar zcvf FileName.tar.gz DirName

need to try it：（not sure）
*.tar.gz和*.tgz 用 tar –xzf 解压
*.tar 用 tar –xvf 解压


 rar：

	rar a all *.jpg
	unrar e all.rar
zip：
			
	zip -r myfile.zip ./*
	unzip -d dir myfile.zip //解压到dir目录下

### 查看系统架构等命令
1. 查看cpu架构

	lscpu    
2. 显示机器名，操作系统和内核的详细信息。：

	uname -a  //命令就是Unix Name的简写。

3. 查看操作系统的发型版本：（eg：CentOS version 7）：
	
	lsb_release -a：
	

具体每项的解释，如下图：
![](/images/uname.png)

### 库相关的命令
1. 目标代码打包成库 ：

	ar -ru *.o 
2. nm -D libiomp5.a

3.来查看一个静态库由那些.o文件构成。

	ar -t libname.a 
4. 可以查看这个可执行文件依赖的so文件。

	ldd ./test

##测试相关命令（提交作业等）
1. nohup command & 。
表示后台提交任务，执行。当退出终端时，用exit退出，nohup提交的任务还会在后台执行。输出结果在nohup.out里面。


	（1）可以使用 jobs 查看后台执行的任务。
	（2）用fg或%可以打开最后一个后台执行的任务。
	（3）可以使用 fg %进程id 关闭后台执行的任务。
	（4）tail -f filename.txt  
	//显示filename.txt文件的最后十行。且若filename.txt在动态变化，输出也会动态变化，每次都输出当前的后十行。ctrl+c可以终止显示。

2. head：

   tail：


	（1）tail -n 20 filename.txt //显示filename.txt文件的最后20行。-n代表读取的起始行。后面紧跟的数字若为+20,表示从文件头开始的第20行。如没有符号，或者为-20，表示从文件尾部开始的第20行。
	（2）tail -c 200 filename.txt //-c表示字节。从filename.txt文件尾部的的第200字节处，开始显示。

more：  
less：

### set，export与source区别：

### PATH，LD_LIBRARY_PATH:

统计文件夹下所有文件中的c代码的行数：
find . -name '*.c' | xargs wc -l {}



### shell的区块注释

https://www.cnblogs.com/emanlee/p/3749911.html

	:<<eof
	被注释的多行内容 
	eof


### Vim 复制粘帖格式错乱问题的解决办法

https://www.cnblogs.com/jianyungsun/archive/2012/07/31/2616671.html

运行如下命令，进入 paste 模式：

	:set paste

进入 paste 模式后，按 i 键进入插入模式，然后再粘帖，文本格式不会错乱了。但粘帖后还需要按 <ESC> 进入普通模式并执行如下命令结束 paste 模式：

	:set nopaste

显然，这样非常麻烦。下面我们进行改进。


## 查一个bin可执行文件的path在哪里的命令：


## linux中uptime命令查看linux系统负载：


![](/images/linux/uptime-command.png)


## diff

diff file_1 file_2

-b:忽略空格带来的影响；
-B：忽略空行造成的不同

[如何查看diff的结果](http://www.ruanyifeng.com/blog/2012/08/how_to_read_diff.html)


## set -e

告诉bash，若执行脚本的过程中，有error，则退出。


### shell写for循环，测试时使用

