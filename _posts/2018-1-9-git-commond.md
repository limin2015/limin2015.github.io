---
layout: post
title:  git命令清单
keywords: git commond
categories : [tools]
tags : [tools]
---


# 整理一下用到的git命令

http://www.ruanyifeng.com/blog/2015/12/git-cheat-sheet.html

# 我的使用

1.在git上新建一个repo。

2.然后在本地: git clone **.git

3.在本地开始修改一些内容，然后每次修改过之后，可以提交到远程仓库：

	git add .
	git commit -m "commit-log"
	git push

4.若远程仓库的内容和本地不是一致的，需要把远程仓库的内容拉取下来：
	
	git fetch origin master
	git log -p master..origin/master ##比较本地分支与远程分支的差别
	git merge origin/master ## 合并本地分支与远程分支


注意：以上的操作都是没有新建分支的情况下。

一般git clone 一个repo后，他的master分支，可能和其他的分支不一样。
可以抓取其中一个分支的内容到本地的新建分支：
	
	git checkout –b lm origin/jxue  //把远程仓库的jxue分支的代码同步到本地的新建的lm分支下



# 一些常用到的命令

显示暂存区和工作区的差异
	
	$ git diff


# 分支相关的命令

列出所有本地分支
	
	$ git branch

列出所有远程分支
	
	$ git branch -r

列出所有本地分支和远程分支
	
	$ git branch -a

新建一个分支，但依然停留在当前分支
	
	$ git branch [branch-name]

新建一个分支，并切换到该分支
	
	$ git checkout -b [branch]

新建一个分支，指向指定commit
	
	$ git branch [branch] [commit]

新建一个分支，与指定的远程分支建立追踪关系
	
	$ git branch --track [branch] [remote-branch]

切换到指定分支，并更新工作区
	
	$ git checkout [branch-name]

切换到上一个分支
	
	$ git checkout -

建立追踪关系，在现有分支与指定的远程分支之间
	
	$ git branch --set-upstream [branch] [remote-branch]

合并指定分支到当前分支
	
	$ git merge [branch]

选择一个commit，合并进当前分支
	
	$ git cherry-pick [commit]

删除分支
	
	$ git branch -d [branch-name]

删除远程分支
	
	$ git push origin --delete [branch-name]
	$ git branch -dr [remote/branch]