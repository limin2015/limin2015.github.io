---
layout: post
title:  c++的一些特性(new to me)
keywords: c++语言
categories : [codingLanguage]
tags : [c++]
---

### traits特性：2017.12.12（TODO）



# 智能指针

**解决的问题**：

防止忘记调用delete；
异常安全；


https://www.cnblogs.com/lanxuezaipiao/p/4132096.html

**如何使用**：

[unique_ptr](http://zh.cppreference.com/w/cpp/memory/unique_ptr)

shared_ptr：



#  emplace_back与push_back区别（vector的成员函数）

http://en.cppreference.com/w/cpp/container/vector/emplace_back



# 求powi的一段代码，写的不错：

	
		static inline double powi(double base, int times)
 		{
  			double tmp = base, ret = 1.0;
  
  			for(int t=times; t>0; t/=2)
     		{
       			if(t%2==1) ret*=tmp;
       			tmp = tmp * tmp;
     		}
     		return ret;
   		}



# 小知识点

1.using F = float; //相当于#define，宏定义
