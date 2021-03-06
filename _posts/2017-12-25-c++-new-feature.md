---
layout: post
title:  c++的一些特性(new to me)
keywords: c++语言
categories : [codingLanguage]
tags : [c++]
---




#  emplace_back与push_back区别（vector的成员函数）

http://en.cppreference.com/w/cpp/container/vector/emplace_back







# 智能指针

**解决的问题**：

防止忘记调用delete；
异常安全；


https://www.cnblogs.com/lanxuezaipiao/p/4132096.html

**如何使用**：

[unique_ptr](http://zh.cppreference.com/w/cpp/memory/unique_ptr)

shared_ptr：






# Lambda表达式 

C++ 11中Lambda表达式的标准形式是：

 [外部变量](参数)->返回值 {函数体}

其中““->返回值”部分可以省略，如果省略则会有返回值类型推导。（类型推导在后面auto中会进行说明）

![](/images/codingLanguage/c++-lamda-1.png)


eg-1:

		int first = 0;  
		int second = 0;  
		int third = 1;  
		  
		int result = [first, &second](int p)->int{  
		     //first++;  改变值传递的外部参数，编译器会报错  
		     second++;  
		     return first + second + p;  
		}(third);  

结果：first = 0, second = 1, result = 2




# 自动类型推导auto





# 初始化语法


通过{}来进行初始化，有如下特性(以前C++是不支持的)：

	int* x = new int[2]{1, 2};  
	vector<int> v = {1, 2};  

另外还支持java方式的初始化：

	class tempObj {  
	public:  
	     int x = 10;  
	};  


但有一些约束调试：看一下知乎上蓝色的博文。



# delete 和 default 函数

比如以前C++的类一旦定义了构造函数，就不再支持默认构造函数，C++ 11可以通过default来实现。
delete告诉编译器不自动产生默认函数，default恰恰相反，它让编译器产生一个默认函数。

eg：
	class NewObj  
	{  
    	NewObj() = default; // 使用默认构造函数  
    	NewObj(int value);  
	};  



# nullptr

C++11里，指针初始化都应该设为nullptr。

看一下知乎上蓝色的博文。




# using进行宏定义

1.using F = float; //相当于#define，宏定义






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



# 引用

1. http://blog.csdn.net/my_business/article/details/7477615




# typename的使用

1. 用在模板的形式参数中，表示var_name是一个数据类型（普通数据类型或者自定义类型）。于class完全一样的效果。

template < typename var_name  > 
class class_name; 

2. typename var_name;表示var_name的定义还没有给出，这个语句通常出现在模版的定义内,例如：

	template <class T>
	void f() {
	typedef typename T::A TA;     // 声明 TA 的类型为 T::A
	TA a5;                      // 声明 a5 的类型为 TA
	typename T::A a6;             // 声明 a6 的类型为 T::A
	TA * pta6;                     // 声明 pta6 的类型为 TA 的指针
	}

	因为T是一个模版实例化时才知道的类型，所以编译器更对T::A不知所云，为了通知
	编译器T::A是一个合法的**类型**，不是类的成员，使用typename语句可以避免编译器报错。


