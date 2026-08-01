# Linked List Cycle 


# Brute Force Solution

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next is not None:
            temp = temp.next

        temp.next = new_node

    def traverse(self):
        temp = self.head
        while temp is not None:
            print(temp.data, end=" ")
            temp = temp.next
        print()

    def cycle(self):
        temp = self.head
        my_set = set()

        while temp is not None:
            if temp in my_set:
                return True

            my_set.add(temp)
            temp = temp.next

        return False


# Driver Code
sll = SinglyLinkedList()

sll.append(10)
sll.append(20)
sll.append(30)
sll.append(40)
sll.append(50)

print(sll.cycle())



# Optimal Solution

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next is not None:
            temp = temp.next

        temp.next = new_node

    def traverse(self):
        temp = self.head
        while temp is not None:
            print(temp.data, end=" ")
            temp = temp.next
        print()

    def cycle(self):
        slow=self.head
        fast=self.head

        while fast is not None and fast.next is not None:
            slow=slow.next
            fast=fast.next.next

            if slow==fast:
                return True
        return False


       


# Driver Code
sll = SinglyLinkedList()

sll.append(10)
sll.append(20)
sll.append(30)
sll.append(40)
sll.append(50)

print(sll.cycle())

