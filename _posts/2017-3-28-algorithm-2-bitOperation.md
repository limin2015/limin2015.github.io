---
layout:     post
title:      algorithm-series-2(位操作专题)
keywords:   algorithm,leetcode
category:   algorithm
tags:       [algorithm]
---
前言：

整理leetcode上刷的算法题目。

### 1，	Power of Two

**题目：**
Given an integer, write a function to determine if it is a power of two.
	
**分析：**
位中只有一个1的数，是2的幂次。如何判断只有一个1？
（1）一个位一个位的，与1 进行&操作。只要每次判断最低位是否为1，然后向右移位，最后统计1的个数即可判断是否是2的次方数
（2）如果一个数是2的次方数的话，根据上面分析，那么它的二进数必然是最高位为1，其它都为0，那么如果此时我们减1的话，则最高位会降一位，其余为0的位现在都为变为1，那么我们把两数相与，就会得到0。

**代码：**
```
方式一：用计数器来数1的个数。
class Solution{
  public:
    bool isPowerOfTwo(int n){
        if(n <= 0)
            return false;
        int count = 0;
        while(n){
            count += n&1;
            n = n>>1;
        }
if(count == 1)
            return true;
        return false;
    }
};

```
**代码：**
```
方式二：class Solution {
public:
    bool isPowerOfTwo(int n) {
        int temp = n-1;
        if(n<=0)
            return false;
        if((temp & n) == 0 )//bracket, because temp&n ==0 -> temp &(n==0)
            return true;
        else
            return false;
    }
};//at first, i forget the corner value: when n<=0, return false;
```


### 2，	Number of 1 Bits

**题目：** 
Write a function that takes an unsigned integer and returns the number of ’1' bits it has (also known as the Hamming weight).
For example, the 32-bit integer ’11' has binary representation 00000000000000000000000000001011, so the function should return 3.
注：汉明距离：
https://zh.wikipedia.org/wiki/%E6%B1%89%E6%98%8E%E9%87%8D%E9%87%8F
	
**分析：**

分析：数二进制位中1的个数，与上题的解法相同。



### 3，	Missing Number

**题目：** 

	
**分析：**






