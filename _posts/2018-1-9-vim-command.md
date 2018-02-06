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




3. tag的使用：

用ctags命令生成tag文件，方便看源代码。

https://blog.easwy.com/archives/advanced-vim-skills-use-ctags-tag-file/

下载vim的中文手册，好好学习一下高级功能，加快开发速度。

