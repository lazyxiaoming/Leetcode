# encoding=utf8
"""
@Module: 
@Author: lionel.ming@foxmail.com
@Time: 2019-12-08 19:01
"""

class Solution:
    def getIntersectionNode(self, headA, headB):
        if not headA or not headB:
            return None
        resA = headA
        resB = headB
        while resA != resB:
            flag = 0
            if resA:
                resA = resA.next
            else:
                flag += 1
                resA = headB
            if resB:
                resB = resB.next
            else:
                resB = headA
            if flag == 2:
                return None
        return resA
