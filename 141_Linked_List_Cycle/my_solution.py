# encoding=utf8
"""
@Module: 
@Author: lionel.ming@foxmail.com
@Time: 2019-12-10 23:39
"""


class Solution:
    def hasCycle(self, head):
        if not head:
            return False
        slow = head
        fast = head.next
        while fast and fast.next and fast != slow:
            fast = fast.next.next
            slow = slow.next
        if not fast or not fast.next:
            return False
        else:
            return True
