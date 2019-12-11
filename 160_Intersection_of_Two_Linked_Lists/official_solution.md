[160. Intersection of Two Linked Lists（两链表的交叉点）](https://leetcode.com/problems/intersection-of-two-linked-lists/)

#### 思路
`A` = [a1, a2, c1, c2, c3]  
`B` = [b1, b2, b3, c1, c2, c3]  
`A+B` = [a1, a2, c1, c2, c3, b1, b2, b3, c1, c2, c3]  
`B+A` = [b1, b2, b3, c1, c2, c3, a1, a2, c1, c2, c3]  

很明显，交叉点在`A+B`和`B+A`的第一个相同处出现。  
这样就可以实现`O(1)`的空间复杂度。
