## Insert at a Specific Position


class Node:
    def __init__(self,val):
        self.val=val
        self.next=None

class SinglyLinkedList: 

    def __init__(self):
        self.head = None
        
    def traverse(self):
            if not self.head:
                print("Sll is empty")
            else:
                current=self.head
                while current is not None:
                    print(current.val , end=" ")
                    current=current.next
                print()

    def insert_at(self,val,position):
        new_node=Node(val)

        if position ==0:
            new_node.next=self.head
            self.head=new_node
        else:
            current=self.head
            prev_node=None
            count=0
            while current is not None and count < position:
                prev_node= current
                current=current.next
                count+=1
            prev_node.next=new_node
            new_node.next=current


