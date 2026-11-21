
"""
Day 128 - Part 180
Introduction to Priority Queues using Binary Heaps

1. Priority Queue
   - Elements are processed according to priority.
   - Not necessarily FIFO.

2. Min Heap
   - Parent <= Children
   - Smallest element is at the root.

3. Max Heap
   - Parent >= Children
   - Largest element is at the root.

4. Binary Heap
   - A complete/almost complete binary tree.
   - Usually implemented using an array.

5. Array Representation (0-based indexing)
   - Parent:      (i - 1) // 2
   - Left Child:  2 * i + 1
   - Right Child: 2 * i + 2

6. Time Complexity
   - Peek:       O(1)
   - Insert:     O(log N)
   - Extract:    O(log N)
   - Build Heap: O(N)

7. Python heapq
   - Implements a Min Heap by default.
   - heappush(): Insert an element.
   - heappop(): Remove the smallest element.
   - heapify(): Convert a list into a heap.
"""

import heapq

min_heap = []

heapq.heappush(min_heap, 30)
heapq.heappush(min_heap, 10)
heapq.heappush(min_heap, 20)

print("Min Heap:", min_heap)
print("Smallest element:", heapq.heappop(min_heap))

# Max Heap using negative values
max_heap = []

for value in [30, 10, 20]:
    heapq.heappush(max_heap, -value)

print("Largest element:", -heapq.heappop(max_heap))
