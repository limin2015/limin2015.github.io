---
layout:     post
title:      algorithm-series-1(array related)
keywords:   algorithm,leetcode
category:   algorithm
tags:		[algorithm]
---
前言：

把之前leetcode上刷的算法题目整理出来。

### 1，（27） Remove Element

**题目：**
	Given an array and a value, remove all instances of that value in place and return the new length.
	Do not allocate extra space for another array, you must do this in place with constant memory.
	The order of elements can be changed. It doesn't matter what you leave beyond the new length.
	**Example:**
		
	Given input array nums = [3,2,2,3], val = 3
	Your function should return length = 2, with the first two elements of nums being 2.

**分析：**

双指针。 i指针从头查找不是val的数， j下标表示当前这是第几个非val，（当前非val的实际存储地址）。

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

## 2，（26） Remove Duplicates from Sorted Array
**题目：**

Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.
Do not allocate extra space for another array, you must do this in place with constant memory.
**For example,**

	Given input array nums = [1,1,2],
	Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively. It doesn't matter what you leave beyond the new length.
	
**分析：**

在一个排序好的数组里面删除重复的元素。双指针方法。i循环遍历数组，若与前一个元素不同，则复制到应该的位置（j的位置）。j指示不重复元素的实际下标。

**代码：**
```
class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        if(nums.size()<=0) return 0;//attention!!

        int j = 1;
        int i;
        for(i=1; i<nums.size(); i++){
            if(nums[i] != nums[i-1]){
                nums[j] = nums[i];
                j++;
            }
        }
        return j;
    }
};
```
## 3，（80） Remove Duplicates from Sorted Array II
**题目：**

Follow up for "Remove Duplicates":
What if duplicates are allowed at most twice?
**For example,**

	Given sorted array nums = [1,1,1,2,2,3],
	Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3. It doesn't matter what you leave beyond the new length.

	
**分析：**

这道题需要分情况。还是双指针，需要加一个计数器count。J指针满足要求的元素实际存储的位置。I用来遍历数组。用当前元素与之前的相同与否来分类。当前元素与之前的相同时，不同时两种情况。相同时，count累加，同时，若count小于等于2时，复制。刚开始我用赋值，不赋值，两种情况分类，发现逻辑搞不清楚啦。

**代码：**
```
class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        if(nums.size()<=0) return 0;
        int j = 1;
        int i;
        int count = 1;
        for(i=1 ; i<nums.size(); i++){
           if(nums[i] == nums[i-1]){
               count ++;
               if(count <= 2) //at first, i mistakely use count<2;
                 nums[j++] = nums[i];
           }
           else{
               count = 1;
               nums[j++] = nums[i];   
           }
        }
         return j;
    }
};
```
## 4，	66. Plus One
**题目：** 

Given a non-negative integer represented as a non-empty array of digits, plus one to the integer.
You may assume the integer do not contain any leading zero, except the number 0 itself.
The digits are stored such that the most significant digit is at the head of the list.
	
**分析：**
模拟加法进位问题，新建一个vector存储结果（大小与原数组相同）。若最高位有进位，则存储需要多一个，在首地址处insert一个元素即可。

**代码：**
```
class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        vector<int> res(digits.size(), 0);
        int i;
        int one = 1;
        int temp;
        for(i = digits.size()-1; i>=0; i--){
            temp = digits[i] + one;
            one = temp / 10;
            res[i] = temp % 10;
        }
        if(one > 0)
            res.insert(res.begin(), one);
        return res;
    }
};
```

## 5，	118. Pascal's Triangle（三角形）
**题目：** 
Given numRows, generate the first numRows of Pascal's triangle.
For example, given numRows = 5,
Return
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
	
**分析：**
a[i][j] = a[i-1][j] + a[i-1][j-1];
以前我做的时候，是把整个矩阵都算出来，把对角线上面的一斜行补零，除了第一列之外，都用公式计算。其实只算下三角就行，只不过每一行的第一个元素和最后一个元素初始化为1，其他元素用公式计算。

**代码：**
```
class Solution {
public:
    vector<vector<int>> generate(int numRows) {
        vector<vector<int>> val;
        val.resize(numRows);
        int i, j;
        for(i=0; i<numRows; i++){
            val[i].resize(i+1);//nElement in i row.
            val[i][0] = 1;//initinization.
            val[i][i] = 1;
            for(j=1; j<i; j++){//deal with middle element.
                val[i][j] = val[i-1][j] + val[i-1][j-1];
            }
        }
        return val;
    }
};
```