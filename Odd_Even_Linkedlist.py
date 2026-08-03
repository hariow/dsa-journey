# Rearranging Nodes

# Brute Force 

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class SinglyLinkedList:

    def __init__(self):
        self.head = None

    def rearrange(self):

        if self.head is None or self.head.next is None:
            return self.head

        values = []

        temp = self.head

        # Odd positions
        while temp:
            values.append(temp.val)
            temp = temp.next
            if temp:
                temp = temp.next

        # Even positions
        temp = self.head.next

        while temp:
            values.append(temp.val)
            temp = temp.next
            if temp:
                temp = temp.next

        temp = self.head
        index = 0

        while temp:
            temp.val = values[index]
            index += 1
            temp = temp.next

        return self.head


# Optimal Solution

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class SinglyLinkedList:

    def __init__(self):
        self.head = None

    def rearrange(self):

        if self.head is None or self.head.next is None:
            return self.head

        odd=self.head
        even=self.head.next
        even_head=even

        while even is not None and even.next is not None:
            odd.next=odd.next.next
            odd=odd.next
            even.next=even.next.next
            even=even.next

        odd.next=even_head
        return self.head