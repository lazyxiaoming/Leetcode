# encoding=utf8
"""
@Module: recursive solution of NO.543
@Author: haoyanming@baidu.com
@Time: 2019-12-03 23:37
"""


class Solution:
    op = 0

    def diameterOfBinaryTree(self, root):
        maxdepth = self.max_depth(root)
        return self.op

    def max_depth(self, root):
        if not root:
            return 0
        maxdepth_left = self.max_depth(root.left)
        maxdepth_right = self.max_depth(root.right)
        maxdepth = max(maxdepth_left, maxdepth_right) + 1
        diameter = maxdepth_left + maxdepth_right
        self.op = max(self.op, diameter)
        return maxdepth
