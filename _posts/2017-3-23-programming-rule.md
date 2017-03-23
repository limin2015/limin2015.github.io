---
layout:     post
title:      编程规范
keywords:   algorithm, rule
category:   algorithm
tags:		[algorithm]
---

前言：以下是我在编程过程中，总结的一些比较有用的编程规范。良好规范的代码习惯，可以帮助减少很多不必要的debug。

规范化编程：

1．	检查内部函数，或者自定义函数的参数的有效性。

2．	malloc完之后，要检查返回的指针是否为NULL，判断是否申请成功。

3．	两个浮点数判断是否相等：fabs(a-b)<eps(可以设置eps为非常小的数：1e-6)

4．	判断一个整数是否是为奇数，用：x%2 != 0(不要用x%2 ==1, 因为x可能为负数)

5．	当使用char类型做数组下标时，因为char有可能为负数，需要将它先强制转化为unsigned char。

6．	Leetcode刷题时，别忘了看返回值的类型。
