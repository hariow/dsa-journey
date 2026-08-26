### dequeue

from collections import deque

lst = deque([])

lst.append(100)
lst.append(200)
lst.append(300)
lst.appendleft(1)   ## append on leftmost
lst.appendleft(3)

print(lst)
lst.popleft()      ## left most removes

print(lst)