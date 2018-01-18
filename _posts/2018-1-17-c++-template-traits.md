---
layout: post
title:  c++的模板和traits特性
keywords: c++语言
categories : [codingLanguage]
tags : [c++]
---

# c++的模板编程


## 函数模板

1. 


        //函数模板---使用体现：调用函数时传递的参数类型。（下面的class关键字可以改成typename）

        template<class 数据类型参数标识符>
        <返回类型><函数名>(参数表)
        {
            函数体
        }

2. 函数模板的特化：

当函数模板需要对某些类型进行特别处理，称为函数模板的特化。

有两个例子：（这两个例子我试过了，OK）
    http://blog.csdn.net/gatieme/article/details/50953564



## 类模板

1. 

        //类模板---使用体现：声明类对象时 Stack<类型> s;
        template<class T>
        class Stack
        {
        　public:
        　　T pop();
        　　bool push(T e);
        　private:
        　　StackNode<T> *p;
        }

        template<class T>//类模板外的 成员函数实现
        T Stack<T>::pop()
        {...}

2. 类模板的三种特化：

http://blog.csdn.net/kybd2006/article/details/1873803

或者：http://www.cppblog.com/SmartPtr/archive/2007/07/04/27496.html






## 结构体模板

    下面的这个没看懂！！！

        //结构体模板---使用体现：声明结构元素时 StackNode<类型> s;
        template<class T>
        struct StackNode
        {
        　　struct T data;
        　　struct StackNode<T> *next;
        };




# traits特性：

1. 是什么？什么时候有使用的需求？

当函数，类或者一些封装的通用算法中的某些部分会因为数据类型不同而导致处理或逻辑不同（而我们又不希望因为数据类型的差异而修改算法本身的封装时），traits会是一种很好的解决方案。（很抽象，没懂！！！）


我的理解：因为模板参数的类型不同，可能会影响到模板中具体的算法时，建立一个新的模板类，然后通过类的模板的特化(全特化、偏特化均可，至少有一个模板形参不同即可)来分别实现其不同。



这篇博客讲的非常清楚：

http://blog.csdn.net/my_business/article/details/7891687