#  Remove Duplicates from a Sorted Doubly Linked List

class Node:
    def __init__(self,val):
        self.value=val
        self.prev=None
        self.next=None

class DoublyLinkedList:
    def __init__(self):
        self.head=None

    def rmv_duplicate(self):

        current=self.head

        while current is not None and current.next is not None:

            if current.data==current.next.data:
                duplicate=current.next
                current.next=duplicate.next

                if duplicate.next is not None:
                    duplicate.next.prev=current

            else:
                current=current.next

        return self.head

                             