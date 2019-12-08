[437. Path Sum III（树路径和Ⅲ）](https://leetcode.com/problems/path-sum-iii/)

#### 思路
1. 要获取树及其子树所有可能的路径之和，然后计数得结果。
2. 利用递归遍历树及其所有子树，获取路径之和列表。

#### 定义
1. `num`：路径之和为`sum`的个数，即题目输出。
2. `sum_list`：一个树自身的路径之和列表。

#### 公式
1. 考虑一个树`root`，`sum_list = [root.val] + [root.val+i for i in sum_list(root.left)] + [root.val+i for i in sum_list(root.right)]`