# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        dummy=ListNode(-1)
        tail=dummy

        while list1 is not None and list2 is not None:

            if list2.val >= list1.val:
                tail.next = list1
                list1 = list1.next

            else:
                tail.next = list2
                list2 = list2.next
            
            tail=tail.next

        tail.next = list1 if list1 is not None else list2
        
        return dummy.next
       

        