# Implement Stack using Doubly Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class MyStack:
    def __init__(self):
        self.top = None

    # Push: Insert at the top

    def push(self, data):
        new_node = Node(data)

        # New node points to current top

        new_node.next = self.top

        # Current top points back to new node

        if self.top is not None:
            self.top.prev = new_node

        # Move top to new node

        self.top = new_node

    # Pop: Remove from top

    def pop(self):
        if self.top is None:
            return -1

        popped = self.top.data

        # Move top to next node

        self.top = self.top.next

        # New top has no previous node

        if self.top is not None:
            self.top.prev = None

        return popped

    # Peek: Return top element

    def peek(self):
        if self.top is None:
            return -1

        return self.top.data

    # Check whether stack is empty

    def is_empty(self):
        return self.top is None

stack = MyStack()

stack.push(10)
stack.push(20)
stack.push(30)

print("Top element:", stack.peek())

print("Popped:", stack.pop())
print("Popped:", stack.pop())

print("Top element:", stack.peek())

print("Is stack empty?", stack.is_empty())

print("Popped:", stack.pop())
print("Popped:", stack.pop())  # Empty → -1