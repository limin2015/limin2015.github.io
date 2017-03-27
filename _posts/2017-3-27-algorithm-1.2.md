---
layout:     post
title:      algorithm-series-1.2(array related)
keywords:   algorithm,leetcode
category:   algorithm
tags:       [algorithm]
---
前言：

把之前leetcode上刷的算法题目整理出来。

### 6，  Pascal's Triangle II

**题目：**
  Given an index k, return the kth row of the Pascal's triangle.
For example, 

    **Example:**
    given k = 3,
    Return [1,3,3,1].
Note:
    Could you optimize your algorithm to use only O(k) extra space?
    
**分析：**
只用一维数组进行操作。从后往前进行计算。初始时，都初始化为1。
第一个代码：（超时啦：）
找到原因：j下标，误写成i啦。导致循环一直在执行，超时。
**代码：**
```class Solution {
public:
    vector<int> getRow(int rowIndex) {
       vector<int> val(rowIndex+1, 1);
       int i, j;
       for(i=2; i<=rowIndex; i++)
        for(j=i-1; i>=1; i--){
            val[j] = val[j] + val[j-1];
        }
        return val;
    }
};
```
**正确代码：**
```
class Solution {
public:
    vector<int> getRow(int rowIndex) {
       vector<int> val(rowIndex+1, 1);
       
       int i, j;
       for(i=2; i<=rowIndex; i++)
        for(j=i-1; j>=1; --j){
            val[j] = val[j] + val[j-1];
        }
        return val;
    }
};
```


## 7，   Merge Sorted Array
**题目：**
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2. The number of elements initialized in nums1 and nums2 are m and n respectively.
    
**分析：**
最原始的做法是，将最后的结果存储到一个新的结果数组中。i，j分别指向两个数组的首部，挨个比较，把小的放到结果数组中。但是，因为多了一个假定，nums1有足够的空间，把它当做结果数组即可。故，需要从后往前遍历，i，j指针指向两数组的尾部，取最大值放到结果数组的相应位置k（k从后往前，指示结果数组中元素的下标）。

**代码：**
```
class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        int k = m+n-1;
        int j = n-1;
        int i = m-1;
        while(i>=0 && j>=0){
            if
        }
    }
};
```
## 8，   Sum
**题目：**
Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.
**For example,**
    
    Example:
    Given a = 1 and b = 2, return 3.
    
**分析：**
不使用加减法，实现加法。肯定得用位操作啦。
不过我不知道怎么用。

查阅发现：
（1）a^b（a，b为两个整数，结果表示a+b的结果位，不算进位）。
（2） a&b(左移一位表示a+b的进位)。

**代码：**
```
方式1：class Solution {
public:
    int getSum(int a, int b) {
        return (b==0) ? a: getSum(a^b, (a&b)<<1);
    }
};
方式2：
class Solution {
public:
    int getSum(int a, int b) {
        if(b == 0)
            return a;
        while(b){
            a = a^b;     (1)
            b = (a&b)<<1; (2)
        }
        return a;
    }
};
```
上面的方式二程序有bug。因为(2)式中的a已经是结果了，不是原来的数a啦。所以需要用一个临时变量算算。
正确的应该是：
```
class Solution {
public:
    int getSum(int a, int b) {
        if(b == 0)
            return a;
        int c;
        while(b){
            c = a^b;
            b = (a&b)<<1;
            a = c;
        }
        return a;
    }
};
```

## 9，   2Sum


**题目：** 


    
**分析：**

**代码：**
```

```

## 10，  3Sum
**题目：** 

    
**分析：**


**代码：**
```

```

## 11，   4Sum


**题目：** 


    
**分析：**

**代码：**
```

```

## 12，  kSum
**题目：** 

    
**分析：**


**代码：**
```

```

