---
layout:     post
title:      algorithm-series-3(树专题)
keywords:   algorithm,leetcode
category:   algorithm
tags:       [algorithm]
---
前言：

整理leetcode上刷的算法题目。

树的遍历：

### 1，105. Construct Binary Tree from Preorder and Inorder（中序）Traversal
**题目：**
Given preorder and inorder traversal of a tree, construct the binary tree.
Note:
You may assume that duplicates do not exist in the tree.
Subscribe to see which companies asked this question.

	
**分析：**
我会用笔分析，但是不会写代码。
解决方案：
画个树，写出前序，中序，看着写即可。
**代码：**
```
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

class Solution {
public:
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        //if vector is null, can begin() work???
        return buildTree(begin(preorder), end(preorder), begin(inorder), end(inorder));
    }
    template<typename T>
    TreeNode* buildTree(T pre_first, T pre_last, T in_first, T in_last){
        if(pre_first == pre_last) return nullptr;
        if(in_first == in_last) return nullptr;
        
        auto root = new TreeNode(*pre_first);
        auto inPos = find(in_first, in_last, *pre_first);//
        int leftLen = distance(in_first, inPos);
        //pre_first + 1 ~~ (pre_first + leftLen),  
        root->left = buildTree(next(pre_first), next(pre_first, leftLen + 1), in_first, next(in_first, leftLen))；
        root->right = buildTree(next(pre_first, leftLen + 1), pre_last, next(inPos), in_last);
        return root;
    }
```
注意：next(a, n)表示，从a这个指针开始（包含a），挨个往下找，循环n次，此时指向这个元素的指针。
Vector:  vec [1,2,3]  -> next(begin(vec),1),此时指针指向第一个元素。
-> next(begin(vec),2),此时指针指向第二个元素。
next(begin(vec)),此时指针指向第二个元素。


### 2，	Construct Binary Tree from Inorder and Postorder Traversal

**题目：** 

**分析：**
画一个图，即可。看着图写。如下：

**代码：**
```
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    TreeNode* buildTree(vector<int>& inorder, vector<int>& postorder) {
        return buildTree(begin(postorder), end(postorder), begin(inorder), end(inorder));
    }
    template<typename T>
    TreeNode* buildTree(T post_first, T post_last, T in_first, T in_last){
        if(post_first ==  post_last) return nullptr;
        if(in_first == in_last) return nullptr;
        
        auto root = new TreeNode(*post_last);
        auto inPos = find(in_first, in_last, *post_last);
        int leftLen = distance(in_first, inPos);
        
        //root->left = buildTree(post_first, next(post_first, leftLen), in_first, prev(inPos));
        //root->right = buildTree(next(post_first, leftLen+1), prev(post_last), next(inPos), in_last);
        
        auto post_left_last = next(post_first, leftLen);
        root->left = buildTree(in_first, inPos, post_first, post_left_last);
        root->right = buildTree(next(inPos), in_last, post_left_last, prev(post_last));
        return root;
    }
};

```
note：
before，Have bugs！！！
Ok。end()指针指向结尾元素的下一个元素。

### 3，		Minimum Depth of Binary Tree

**题目：** 

	
**分析：**

### 4，	Maximum Depth of Binary Tree


**题目：** 

	
**分析：**

### 5，	Binary Tree Preorder Traversal


**题目：** 
Given a binary tree, return the preorder traversal of its nodes' values.
For example:
Given binary tree {1,#,2,3},
   1
    \
     2
    /
   3
return [1,2,3].
Note: Recursive solution is trivial, could you do it iteratively?

	
**分析：**
法一，递归遍历easy；
不递归，迭代进行。模拟递归（没写过）。
**代码：**
```
递归代码：
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    void traversal(TreeNode* root, vector<int>& ret){
         if(root == NULL) return ;
        ret.push_back(root->val);
        if(root->left)
            traversal(root->left, ret);
        if(root->right) 
            traversal(root->right, ret);
    }
    
    vector<int> preorderTraversal(TreeNode* root) {
        vector<int> ret;
        traversal(root, ret)
;
        return ret;
    }
};

```

### 6，	 Binary Tree Inorder Traversal

**代码：**
```
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    void traversal(TreeNode* root, vector<int>& ret){
        if(root == NULL) return ;
        if(root->left) traversal(root->left, ret);
        ret.push_back(root->val);//at first, i mistakely write: *root.
        if(root->right) traversal(root->right, ret);
        
    }
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> ret;
        traversal(root, ret);
        return ret;
    }
};
```

### 7，	 Binary Tree Postorder Traversal

**代码：**
```
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    void traversal(TreeNode* root, vector<int>& ret){
        if(root == NULL) return ;
        if(root->left) traversal(root->left, ret);
        if(root->right) traversal(root->right, ret);
        ret.push_back(root->val);
    } 
    vector<int> postorderTraversal(TreeNode* root) {
        vector<int> ret;
        traversal(root, ret);
        return ret;
    }
};

```
### 8，	Minimum Depth of Binary Tree


**题目：** 
Given a binary tree, find its minimum depth.The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
	
**分析：**
递归实现。但是为啥，参数要有兄弟是否为空呢？
因为，保证当root为空时，若root有兄弟，则最小深度并不是0，而是其兄弟那支的最小深度。可以画个图看看。下一题求最大深度的时候，就没有这个问题，不管有没有兄弟都返回0，因为求的是max。

**代码：**
```
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    int solver(TreeNode *root, bool hasBrother){
        if(root == NULL) return hasBrother? INT_MAX: 0;
        
        return 1+min(solver(root->left, root->right != NULL), solver(root->right, root->left != NULL));
        
    }
    int minDepth(TreeNode* root) {
        return solver(root, false);
    }
};
```

### 9，	Maximum Depth of Binary Tree

**题目：** 
Given a binary tree, find its maximum depth.
The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

	
**分析：**
见上题。

**代码：**
```
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    int solver(TreeNode* root){
        if(root == NULL) return 0;
        return 1 + max(solver(root->left), solver(root->right));
    }
    int maxDepth(TreeNode* root) {
        int deep = 0;
        deep = solver(root);
        return deep;
    }
};
```

### 10，	Path Sum

**题目：** 
Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.
For example:
Given the below binary tree and sum = 22,
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.


	
**分析：**


**代码：**
```
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    bool hasPathSum(TreeNode* root, int sum) {
        if(root == NULL)
        	return false;
        if(root->left == NULL &&root->right == NULL)
        	return sum == root->val;
        else
        	return (hasPathSum(root->left, sum-root->val))||(hasPathSum(root->right, sum-root->val));
    }
};
```














