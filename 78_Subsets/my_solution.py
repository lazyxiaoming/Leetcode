# encoding=utf8
"""
@Module: 
@Author: lionel.ming@foxmail.com
@Time: 2019-12-11 23:28
"""

class Solution:
    def subsets(self, nums):
        nums.sort()
        op = [[]]
        res = [i for i in nums]
        for k in range(len(nums)):
            op += res
            res = [i + [j] for i in res for j in nums if j > i[-1]]
        return op
