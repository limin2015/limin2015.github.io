---
layout: post
title:  vim快捷键清单
keywords: sublime
categories : [tools]
tags : [tools]
---


整理一下用到的vim快捷键，便于查阅。


# 1.配置vimrc：
	

		set nocompatible
 		set syntax=on
  		set number
  		set tabstop=4
  		set autoindent
  		set showmatch
  		set cindent
  		filetype on
  		set completeopt=longest,menu
 		set shiftwidth=4
 		set softtabstop=4


# 2.常用快捷键：


移到行尾：

    命令： $

移到行首：

    命令：0

移到文件尾部：
	
	命令：GG

移到文件首部：
		
	命令：gg

复制，黏贴：
	命令：dd然后yy（复制5行是5dd）

按住ctrl+v：区块选中，然后可以yy


将word-1替换成word-2：
 
 	:.,%s/word-1/word-2/gc




移动光标到下一个单词的词首，使用命令"w"，移动光标到上一个单词的词首，使用命令"b"；移动光标到下一个单词的结尾，用命令"e"，移动光标到上一个单词的结尾，使用命令"ge"。



3.区块注释：

法1：

	（1）按CTRL+V进入可视化模式（VISUAL BLOCK）
	（2）移动光标上移或者下移，选中多行的开头
	（3）选择完毕后，按大写的的I键，此时下方会提示进入“insert”模式，输入你要插入的注释符，例如#，
	（4）最后按ESC键，发现多行代码已经被注释了

法2：使用替换命令

	:% s/^/#/g 来在全部内容的行首添加 # 号注释
	:1,10 s/^/#/g 在1~10 行首添加 # 号注释

 ref：
  https://jingyan.baidu.com/article/9c69d48f43ed6d13c8024e7b.html


4. tag的使用：

用ctags命令生成tag文件，方便看源代码。

https://blog.easwy.com/archives/advanced-vim-skills-use-ctags-tag-file/

下载vim的中文手册，好好学习一下高级功能，加快开发速度。

https://jaist.dl.sourceforge.net/project/vimcdoc/pdf-manual/user_manual-2.1.0.pdf




# VS-Code 快捷键：

一般在服务器上都是使用vim编辑器，后来发现，直接在Xftp（本地与服务器传输工具）中，右键打开文件，保存文件，就可以直接作用到服务器上的文件中。故，开始使用vs-code 编辑器，加速开发。

	Ctrl + G
	转到行... Go to Line...
	Ctrl + P
	转到文件... Go to File...
	Ctrl + Shift + O
	转到符号... Go to Symbol...


	Ctrl + F
	查找 Find
	Ctrl + H
	替换 Replace


	Ctrl+X
	剪切行（空选定） Cut line (empty selection)
	Ctrl+C
	复制行（空选定）Copy line (empty selection)


	Ctrl+Shift+K
	删除行 Delete line
	Ctrl+Enter
	在下面插入行 Insert line below
	Ctrl+Shift+Enter
	在上面插入行 Insert line above


	Ctrl+] / [
	缩进/缩进行 Indent/outdent line

	Ctrl+/
	切换行注释 Toggle line comment

	Ctrl+Shift+\
	跳到匹配的括号 Jump to matching bracket

	Home
	转到行首 Go to beginning of line
	End
	转到行尾 Go to end of line
	Ctrl+Home
	转到文件开头 Go to beginning of file
	Ctrl+End
	转到文件末尾 Go to end of file