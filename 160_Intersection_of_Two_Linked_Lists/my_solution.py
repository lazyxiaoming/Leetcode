# encoding=utf8
"""
@Module: 
@Author: haoyanming@baidu.com
@Time: 2019-12-05 23:29
"""


class Solution:
    def getIntersectionNode(self, headA, headB):
        resA = headA
        resB = headB
        l_id_A, l_ListNode_A = self.genlist(resA)
        l_id_B, l_ListNode_B = self.genlist(resB)
        index = self.findcommonsublist(l_id_A, l_id_B)
        if not index:
            return None
        return l_ListNode_A[index]

    def genlist(self, head):
        l_id = []
        l_ListNode = []
        while head:
            l_id.append(id(head))
            l_ListNode.append(head)
            head = head.next
        return l_id, l_ListNode

    def findcommonsublist(self, list1, list2):
        if not list1 or not list2:
            return None
        if list1[-1] != list2[-1]:
            return None
        index = -1
        while list1[index] == list2[index]:
            index -= 1
            try:
                list1[index]
                list2[index]
            except:
                break
        return index + 1
