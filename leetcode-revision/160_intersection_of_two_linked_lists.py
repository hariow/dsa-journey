# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        a = headA
        b = headB

        while a is not b:
            a = headB if a is None else a.next
            b = headA if b is None else b.next
          
            
        return a