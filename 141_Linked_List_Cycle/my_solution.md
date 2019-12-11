[141. Linked List Cycle（有环链表）](https://leetcode.com/problems/linked-list-cycle/)

#### 思路
1. 经典问题，要实现O(1)空间复杂度，设置两个速度不同的节点。如果有环，快节点一定会追上慢节点；否则，快节点最先到达结尾。

#### 定义
1. `fast`：快节点，一次向后移动2个节点
2. `slow`：慢节点，一次向后移动1个节点

