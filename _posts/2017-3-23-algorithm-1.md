---
layout:     post
title:      编程规范
keywords:   algorithm, rule
category:   algorithm
tags:		[algorithm]
---

前言：以下是我在编程过程中，总结的一些比较有用的编程规范。良好规范的代码习惯，可以帮助减少很多不必要的debug。

### 1，（27） Remove Element

**题目：**


	Given an array and a value, remove all instances of that value in place and return the new length.
	Do not allocate extra space for another array, you must do this in place with constant memory.
	The order of elements can be changed. It doesn't matter what you leave beyond the new length.
	Example:
	Given input array nums = [3,2,2,3], val = 3
	Your function should return length = 2, with the first two elements of nums being 2.

**分析：**

双指针。i指针从头查找不是val的数，j下标表示当前这是第几个非val，（当前非val的实际存储地址）

**代码：**
```

class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int i=0, j=0;
        for(i=0; i<nums.size(); i++){
            if(nums[i] == val)
                continue;
            nums[j] = nums[i];
            j++;
        }
        return j;
    }
};

```