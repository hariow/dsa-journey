## queue_using_array

class Queue:
    def __init__(self):
        self.items=[]

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self,item):
        self.items.append(item)

    def dequeue(self):
        if len(self.items) == 0:
            print("dequeue from empty list")
            return
        x=self.items.pop(0)
        return x

    def front(self):
        if len(self.items) == 0:
            print("Cannot peek,list is empty")
            return
        return self.items[0]

    def rear(self):
        if len(self.items) == 0:
            print("Cannot read , queue is empty")
            return
        return self.items[-1]

    def size(self):
        return len(self.items)

queue = Queue()

queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.enqueue(40)

print("Queue:", queue.items)
print("Front:", queue.front())
print("Rear:", queue.rear())
print("Size:", queue.size())

print("Dequeued:", queue.dequeue())
print("Queue after dequeue:", queue.items)

print("Front after dequeue:", queue.front())
print("Is empty:", queue.is_empty())