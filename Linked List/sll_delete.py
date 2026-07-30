## Deleting a Node

class Node:
    def __init__(self,val):
        self.val=val
        self.next=None

class SinglyLinkedList: 

    def __init__(self):
        self.head = None

    def delete(self,val):
        temp=self.head

        if temp.next is not None:
            if temp.val==val:
                self.head=temp.next
                return
            else:
                found=False
                prev=None
                while temp is not None:
                    if temp.val==val:
                        found=True
                        break
                    prev=temp
                    temp=temp.next

                if found:
                    prev.next=temp.next
                    del temp
                    return

                else:
                    print("Node Not Found")