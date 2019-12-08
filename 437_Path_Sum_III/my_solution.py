# encoding=utf8
"""
@Module: 
@Author: lionel.ming@foxmail.com
@Time: 2019-12-08 22:05
"""


class Solution:
    num = 0

    def pathSum(self, root, sum):
        self.sum = sum
        self.num = 0
        self.sum_of_tree(root)
        return self.num

    def sum_of_tree(self, root):
        if not root:
            return []
        sum_list = []
        sum_list.append(root.val)
        sum_list += [root.val + i for i in self.sum_of_tree(root.left)]
        sum_list += [root.val + i for i in self.sum_of_tree(root.right)]
        for i in sum_list:
            if i == self.sum:
                self.num += 1
        return sum_list
