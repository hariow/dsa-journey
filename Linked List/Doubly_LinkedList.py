## Insert at Head

class Node:
    def __init__(self,val):
        self.value=val
        self.next=None
        self.prev=None

class DoublyLinkedList:
    def __init__(self):
       self.head=None

    def insert_at_head(self,val):
        new_node=Node(val)

        if not self.head:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

dll=DoublyLinkedList()
dll.insert_at_head(10)
dll.insert_at_head(20)


## Appending at Last


class Node:
    def __init__(self,val):
        self.value=val
        self.next=None
        self.prev=None

class DoublyLinkedList:
    def __init__(self):
       self.head=None

    def append(self,val):
        new_node=Node(val)

        if not self.head:
            self.head=new_node
        else:
            temp = self.head

            while temp.next is not None:  ## reaches the last element
                temp = temp.next

            temp.next = new_node   ## appending the lasty element
            new_node.prev = temp

# Driver code

dll=DoublyLinkedList()
dll.append(100)



# Insert in Between 

class Node:
    def __init__(self,val):
        self.value=val
        self.next=None
        self.prev=None

class DoublyLinkedList:
    def __init__(self):
       self.head=None

    def insert_at_head(self,val):
            new_node=Node(val)
    
            if not self.head:
                self.head = new_node
            else:
                new_node.next = self.head
                self.head.prev = new_node
                self.head = new_node

    def insert_at(self,val,position):
        new_node = Node(val)
        if position==0:
            self.insert_at_head(val)
            return

        temp = self.head
        count = 0

        while temp and count < position-1:
            temp=temp.next
            count+=1

        if temp is None:
            print("Out of Bounds")
            return 

        new_node.next = temp.next
        new_node.prev = temp

        if temp.next:
            temp.next.prev = new_node

        temp.next = new_node


## Traverse() , delete head() , delete_last() , delete_in_between()



class Node:
    def __init__(self, val):
        self.value = val
        self.next = None
        self.prev = None


class DoublyLinkedList:

    def __init__(self):
        self.head = None

    # ---------------- Traverse ------------------
    def traverse(self):
        if self.head is None:
            print("DLL is Empty")
            return

        temp = self.head

        while temp is not None:
            print(temp.value, end=" <-> ")
            temp = temp.next

        print("None")

    # ---------------- Delete Head ----------------
    def delete_head(self):

        if self.head is None:
            return

        self.head = self.head.next

        if self.head is not None:
            self.head.prev = None

    # ---------------- Delete Tail ----------------
    def delete_tail(self):

        if self.head is None:
            return

        if self.head.next is None:
            self.head = None
            return

        temp = self.head

        while temp.next is not None:
            temp = temp.next

        temp.prev.next = None

    # ---------------- Delete at Position ----------------
    def delete_in_between(self, position):

        if self.head is None:
            return

        if position == 1:
            self.delete_head()
            return

        temp = self.head
        count = 1

        while temp is not None and count < position:
            temp = temp.next
            count += 1

        if temp is None:
            return

        if temp.next is None:
            self.delete_tail()
            return

        temp.prev.next = temp.next
        temp.next.prev = temp.prev