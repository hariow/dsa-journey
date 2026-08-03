# Find Length of Loop in Linked List | Floyd Cycle Detection Algo

# Brute Force

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
        travel=0
        my_dict = dict()

        while temp is not None:
            if temp in my_dict:
                return travel-my_dict[temp]
            
            my_dict[temp]=travel
            travel+=1
            temp=temp.next

        return 0


# Driver Code
sll = SinglyLinkedList()

sll.append(10)
sll.append(20)
sll.append(30)
sll.append(40)
sll.append(50)

# Create Cycle (50 -> 30)

temp = sll.head
third = temp.next.next

while temp.next is not None:
    temp = temp.next

temp.next = third

print(sll.cycle())


# Optimal Solution

