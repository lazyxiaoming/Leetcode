[543. Diameter of Binary Tree（二叉树的直径）](https://leetcode.com/problems/diameter-of-binary-tree/)

#### 思路
1. 所求直径实际等于二叉树中的最长路径。  
2. 很明显，对一个二叉树本身来说，不考虑子树的情况下，最长路径应该是左边最深叶子节点经过根节点最后到达右边最深叶子节点的路径。  
3. **但是，二叉树中的最长路径应该是二叉树本身及其所有子树的最长路径中的最大值。**

#### 定义
1. `op`：所求二叉树直径
2. `maxdepth`：二叉树的最大深度（初始深度为1）
3. `maxnodenum`：二叉树中最长路径的节点个数

#### 公式
1. `op = max(maxnodenum) - 1`
2. `maxnodenum = maxdepth_left + maxdepth_right + 1`
3. `maxdepth = max(maxdepth_left, maxdepth_right) + 1`

#### 解法
公式3是一个递归形式，递归过程即遍历了所有子树。  
在递归过程中利用公式2可得每一个子树的最长路径，同时更新所有子树的最长路径的最大值。
递归完成后，利用公式1得到二叉树直径。

#### 踩坑
很容易想到思路1和2，但无法ac。查看不通过case，才发现有子树的最长路径大于二叉树自身的最长路径的情况，从而得到思路3。