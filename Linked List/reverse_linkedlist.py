# Reverse Linked List

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

    def reverse(self):
        temp = self.head
        prev = None

        while temp is not None:
            front = temp.next
            temp.next = prev
            prev = temp
            temp = front

        self.head = prev


# Driver Code
sll = SinglyLinkedList()

sll.append(10)
sll.append(20)
sll.append(30)
sll.append(40)
sll.append(50)
sll.append(20)
print("Original List:")
sll.traverse()

sll.reverse()

print("Reversed List:")
sll.traverse()
