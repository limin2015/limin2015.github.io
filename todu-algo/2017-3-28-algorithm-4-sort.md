---
layout:     post
title:      algorithm-series-4(sort)
keywords:   algorithm,leetcode
category:   algorithm
tags:       [algorithm]
---
前言：

整理leetcode上刷的算法题目。

### 1， 21. Merge Two Sorted Lists
**题目：**

Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.
	
**分析：**
跟merge sorted数组差不多。链表，插入，删除很方便。
**代码：**
```
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        if(l1 == NULL ) return l2;
        if(l2 == NULL ) return l1;
        
        ListNode head(-1);
        ListNode *p = &head;
        
        while(l1 != NULL && l2 != NULL){
            if(l1->val > l2->val){
                p->next = l2;
                l2 = l2->next;
            }else{
                p->next = l1;
                l1 = l1->next;
            }
            p =  p->next;//don't forget.
        }
        p->next = (l1 == NULL? l2 : l1);
        return head.next;
    }
};

```



### 2，	 Merge k Sorted Lists

**题目：** 
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
**分析：**
2个合并成1个，然后在和后面的合并。时间复杂度如何分析？？
并行算法中，logn就可以合并。类似我做的寄存器通信的意思。


**代码：**
```
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        if(l1 == NULL ) return l2;
        if(l2 == NULL ) return l1;
        
        ListNode head(-1);
        ListNode *p = &head;
        
        while(l1 != NULL && l2 != NULL){
            if(l1->val > l2->val){
                p->next = l2;
                l2 = l2->next;
            }else{
                p->next = l1;
                l1 = l1->next;
            }
            p =  p->next;//don't forget.
        }
        p->next = (l1 == NULL? l2 : l1);
        return head.next;
    }

    ListNode* mergeKLists(vector<ListNode*>& lists) {
        if(lists.size() == 0) return nullptr;
        ListNode *ret = lists[0];
        int i;
        //attention: i initilize to 1.
        for(i=1; i<lists.size(); i++){
            ret = mergeTwoLists(ret, lists[i]);
        }
        return ret;
    }
};


```


### 3，Sort a linked list using insertion sort.	

**题目：** 

	
**分析：**
使用插入排序，对链表进行排序。首先，带不带头结点？其次，i指定，开始插哪个元素啦。j指定，在哪个位置插，然后执行链表的插入操作。








