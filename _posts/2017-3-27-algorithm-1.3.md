---
layout:     post
title:      algorithm-series-1.3(array related)
keywords:   algorithm,leetcode
category:   algorithm
tags:       [algorithm]
---
前言：

把之前leetcode上刷的算法题目整理出来。

### 13，	Find Minimum in Rotated Sorted Array

**题目：**
 Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
Find the minimum element.
You may assume no duplicate exists in the array.
	
**分析：**
二分法。分情况来看。但是要注意特殊情况（第3条，4条）
（1）当nums[start] <nums[end],也就是区间有序时，直接返回nums[start]。不用进行二分啦。否则，进行二分。
（2）A[mid] > A[start]， 那么最小值一定在右半区间，[mid+1, end].
（3）A[mid] < A[start], 那么最小值一定在左半区间，[start, mid]。注意包含mid。
特殊情况：
（1）	当只剩两个元素，也就是start + 1 == end时，返回两者之中的小数。此时再二分，按照原来的原则，得不出结论啦。比如[2,1]这种情况。

**代码：**
```
class Solution {
public:
    int findMin(vector<int>& nums) {
        int start = 0; 
        int end = nums.size()-1;//at first, i forget -1. 
        int middle;
        if(nums.size() == 0)
            return 0; 
        while(start < end){//check border.
            if(nums[start] < nums[end])//when ordered, return leftest value. 
                return nums[start];
            if(start+1 == end)//this case deal with: [2,1] 
                //return nums[start]>nums[end]?nums[end]:nums[start];
                return min(nums[start], nums[end]);    
            middle = (start+end)/2;
            if(nums[middle] > nums[start]){//to right side.
                start = middle;//or start = middle + 1
            }
            else{
                end = middle;
            }
        }
        return nums[start];//or end.
    }
};
```


##14，	154. Find Minimum in Rotated Sorted Array II
**题目：**
同上(13)，但是元素可能有重复。
    
**分析：**
二分时，需要考虑nums[mid]和nums[start]是否相等的情况。
此时，跳过start，从区间[start+1, end]开始查找。
注意：重复元素很多时，二分法的运行效率就跟直接遍历整个数组一样啦。


**代码：**
```
class Solution {
public:
    int findMin(vector<int>& nums) {
        if(nums.size() == 0)
            return 0;
        int start = 0; 
        int end = nums.size()-1;
        int mid;
        while(start < end){
            if(nums[start] < nums[end])
                return nums[start];
            if(start + 1 == end)
                return min(nums[start], nums[end]);
            mid = (start + end)/2;
            if(nums[mid] > nums[start])
                start = mid + 1;
            else if(nums[mid] < nums[start])
                  end = mid;
                  else start++;//difference compared with no duplicate.
        }
        return nums[start];
    }
};
```
## 15，	Largest Rectangle in Histogram
**题目：**

**For example,**
	
    
**分析：**


**代码：**
```

```

## 16，	Maximal Rectangle


**题目：** 


    
**分析：**

**代码：**
```

```

## 17，	7. Reverse Integer
**题目：** 
Reverse digits of an integer.
Example1: x = 123, return 321
Example2: x = -123, return -321
click to show spoilers.
Have you thought about this?
Here are some good questions to ask before coding. Bonus points for you if you have already thought through this!
If the integer's last digit is 0, what should the output be? ie, cases such as 10, 100.
Did you notice that the reversed integer might overflow? Assume the input is a 32-bit integer, then the reverse of 1000000003 overflows. How should you handle such cases?
For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
Note:
The input is assumed to be a 32-bit signed integer. Your function should return 0 when the reversed integer overflows.

    
**分析：**
处理方法，依次分离各位，十位，然后累加到result上。
处理特殊情况：
（1）	x为负数时，将负数转换为正数（加负号），再按照通用方法求，最后返回时再取反返回即可。注意：并不是所有的负数都能转换为正数。INT_MIN，无相应的正数对应，针对他单独处理，直接返回0即可（它的逆序overflow）。
（2）	考虑溢出，按照常规方法算出result后，result应该定义为long long，判断它与INT_MAX大小，若整形溢出，则return 0；


**代码：**
```
class Solution {
public:
    int reverse(int x) {
 bool negative_flag=false;//是否为负数
        if(x==INT_MIN)   //这里必须要判断   应为 INT_MIN  为了表示方便用八位 二进制为 1000 0000  进行x=-x运算时，计算机中用补码相乘，-1的补码为原码除符号位外取反加1  也就是 1000 0001  取反加一补码变为 1111 1111，所以x=-x变为补码乘法 1000 0000*1111 1111 =1000 0000，x又等于了INT_MIN ,所以当while循环中的x并没有为正数。
        return 0;
        if(x<0)
        {
            x=-x;
            negative_flag=true;
        }
        long long result=0;
        while(x!=0)
        {
            result=result*10+x%10;
            x=x/10;//核心代码

        }
        if(result>INT_MAX)
            return 0;
        if(negative_flag)
            return -result;
         else
             return result;
    }
};

```
## 18，	Palindrome Number
**题目：** 
Determine whether an integer is a palindrome. Do this without extra space.
click to show spoilers.
Some hints:
Could negative integers be palindromes? (ie, -1)
If you are thinking of converting the integer to string, note the restriction of using extra space.
You could also try reversing an integer. However, if you have solved the problem "Reverse Integer", you know that the reversed integer might overflow. How would you handle such case?
There is a more generic way of solving this problem.
**分析：**
因为不占用多余空间。故不能将int转为string来做啦。（不懂！！）
采取的策略：整数反转，看与原数是否相同。
（1）	负数不是回文。0是回文。
（2）	注意，整数反转，有可能溢出，所以result用long long类型。

**代码：**
```
class Solution {
public:
    bool isPalindrome(int x) {//反转，看与原数是否相等
    if(x<0)
    return false;
        int temp=x;
        long long result = 0;//防止溢出。因为整数inverse maybe溢出。
        while(temp)
        {
            result = result*10 + temp%10;
            temp = temp/10;
        }
        if(result==x)
        return true;
        else
        return false;
    }
};
```
## 19，	Search a 2D Matrix
**题目：** 
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:
Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.

**For example**


	Consider the following matrix:
	[
	[1,   3,  5,  7],
	[10, 11, 16, 20],
	[23, 30, 34, 50]
	]
	Given target = 3, return true.

**分析：**
从左下角开始寻找，若比左下角大，则往右寻找；若小，则往上寻找。

**代码：**
```
class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        //int row = matrix.size();
        //int col = matrix[0].size();
        if(matrix.size() == 0)
            return false;
        if(matrix[0].size()==0)
            return false;
            
        int row = matrix.size();
        int col = matrix[0].size();
        if(row==0 || col == 0) return false;//special case.
        
        int i = row -1;
        int j = 0;
        
        while(i>=0 && j<=col-1){
            if(matrix[i][j] == target) return true;
            if(matrix[i][j] > target) i = i-1;
            else j = j+1;
            
        }
        return false;
    }
};
```
note:
刚开始只有注释地方，没有注释后面的几行，报错啦。原因：若matrix.size()==0，则matrix[0].size()是错误的，操作了NULL指针。故，得一个一个判断。用红色处代码代替即可。

## 20，240. Search a 2D Matrix II
**题目：** 
 Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:
Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.


**For example**
	
	For example,
	Consider the following matrix:
	[
	  [1,   4,  7, 11, 15],
	  [2,   5,  8, 12, 19],
	  [3,   6,  9, 16, 22],
	  [10, 13, 14, 17, 24],
	  [18, 21, 23, 26, 30]
	]
	Given target = 5, return true.
	Given target = 20, return false.

**分析：**
解法与上面一题一模一样。
