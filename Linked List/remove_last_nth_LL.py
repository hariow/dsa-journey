# Remove Nth Node from End of List

class Node:
    def __init__(self,val):
        self.value=val
        self.next=None

class SinglyLinkedList:

    def __init__(self):
        self.head=None

    def remove(self,n):

        length=0
        temp=self.head

        while temp is not None:
            length+=1
            temp=temp.next

        if length==n:
            new_head=self.head.next

            return new_head

        position_to_stop = length-n

        temp=self.head
        count=1

        while count < position_to_stop:
            temp=temp.next
            count+=1

        temp.next=temp.next.next
        return self.head


# Optimal Solution

class Node:
    def __init__(self,val):
        self.value=val
        self.next=None

class SinglyLinkedList:
    def __init__(self):
        self.head=None

    def remove(self,n):

        slow=self.head
        fast=self.head

        for _ in range(n):
            fast=fast.next

        if fast==None:
            return self.head.next

        while fast.next is not None:
            slow=slow.next
            fast=fast.next

        slow.next=slow.next.next

        return self.head
        