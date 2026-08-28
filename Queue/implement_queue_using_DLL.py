# Implement Queue using Doubly Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class MyQueue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.count = 0

    def enqueue(self, x):
        new_node = Node(x)

        # If queue is empty
        if self.rear is None:
            self.front = new_node
            self.rear = new_node
        else:
            new_node.prev = self.rear
            self.rear.next = new_node
            self.rear = new_node

        self.count += 1

    def dequeue(self):
        # If queue is empty
        if self.front is None:
            return -1

        removed = self.front.data

        self.front = self.front.next

        if self.front is None:
            self.rear = None
        else:
            self.front.prev = None

        self.count -= 1

        return removed

    def peek(self):
        if self.front is None:
            return -1

        return self.front.data

    def is_empty(self):
        return self.front is None

    def size(self):
        return self.count


q = MyQueue()

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

print("Front:", q.peek())
print("Removed:", q.dequeue())
print("Removed:", q.dequeue())
print("Front:", q.peek())
print("Size:", q.size())
print("Is empty:", q.is_empty())