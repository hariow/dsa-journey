# Find Pairs with Given Sum in Doubly Linked List 


# Brute Force 

class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None

class DoublyLinkedList:
        def __init__(self):
            self.head=None

        def find_sum(self,target):

            temp1=self.head
            result=[]

            while temp1 is not None:
                temp2=temp1.next

                while temp2 is not None:
                    if temp1.data+temp2.data==target:
                        result.append([temp1.data,temp2.data])
                    temp2=temp2.next

                temp1=temp1.next

            return result
    


## Better Solution

class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None

class DoublyLinkedList:
        def __init__(self):
            self.head=None

        def find_sum(self,target):

            my_set=set()
            temp=self.head
            result=[]

            while temp is not None:
                remaining = target - temp.data

                if remaining in my_set:
                    result.append([remaining,temp.data])
                my_set.add(temp.data)
                temp=temp.next

            return result


## Optimal Solution

class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None

class DoublyLinkedList:
        def __init__(self):
            self.head=None

        def find_sum(self,target):
            result=[]
            left=self.head
            right=self.head

            while right.next is not None:
                right=right.next

            ## If data is not unique than use this:" while left != right and left.prev != right: "
            
            while left is not None and right is not None and left.data < right.data:
                total = left.data + right.data 
                if total==target:
                    result.append([left.data,right.data])
                    left=left.next
                    right=right.prev

                elif total > target:
                    right=right.prev

                else:
                     left=left.next
            return result         
