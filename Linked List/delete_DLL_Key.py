class Node:
    def __init__(self, val):
        self.value = val
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def delete_key(self, key):

        if self.head is None:
            return None

        temp = self.head
        prev = None
        new_head = self.head

        while temp is not None:

            next_node = temp.next

            if temp.value == key:

                if prev is not None:
                    prev.next = temp.next

                if temp.next is not None:
                    temp.next.prev = prev

                if temp == new_head:
                    new_head = new_head.next
                    if new_head is not None:
                        new_head.prev = None

            else:
                prev = temp

            temp = next_node

        return new_head