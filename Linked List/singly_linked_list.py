## Append and Traverse Singly Linked List 

class Node:
    def __init__(self,val):
        self.val=val
        self.next=None

class SinglyLinkedList: 

    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
 
        # if self.head is None:
              
        if self.head is None:
            self.head = new_node  
        else:
            current = self.head

            while current.next is not None:
                current = current.next
            current.next = new_node

    def traverse(self):
        if not self.head:
            print("Sll is empty")
        else:
            current=self.head
            while current is not None:
                print(current.val , end=" ")
                current=current.next
            print()

sll=SinglyLinkedList()
sll.append(10)
sll.append(20)
sll.append(30)
sll.append(40)
sll.traverse()


