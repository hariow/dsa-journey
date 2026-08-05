# Reverse a Doubly Linked List

# Brute Force 

class Node:
    def __init__(self,val):
        self.value=val
        self.next=None
        self.prev=None

class DoublyLinkedList:
    def __init__(self):
       self.head=None

    def reverse(self):
        temp=self.head
        stack=[]

        while temp is not None:
            stack.append(temp.value)
            temp=temp.next

        temp=self.head

        while temp is not None:
            e=stack.pop()
            temp.value=e
            temp=temp.next
        return self.head



# Optimal Solution

class Node:
    def __init__(self,val):
        self.value=val
        self.prev=None
        self.next=None

class DoublyLinkedList:
    def __init__(self):
        self.head=None

    def reverse(self):
        if self.head.next is None:
            return self.head

        current=self.head
        prev=None

        while current is not None:
            front=current.next
            current.next=prev
            current.prev=front

            prev=current
            current=front
        return prev
