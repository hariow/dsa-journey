
class Solution:
    def __init__(self):
        self.arr = []
        self.cnt = 0

    def heapifyup(self, arr, ind):
        parent_idx = (ind - 1) // 2

        if ind > 0 and arr[parent_idx] < arr[ind]:
            arr[parent_idx], arr[ind] = arr[ind], arr[parent_idx]
            self.heapifyup(arr, parent_idx)

        return arr

    def heapifydown(self, arr, ind):
        n = len(arr)
        left_idx = 2 * ind + 1
        right_idx = 2 * ind + 2
        large_idx = ind

        if left_idx < n and arr[large_idx] < arr[left_idx]:
            large_idx = left_idx

        if right_idx < n and arr[large_idx] < arr[right_idx]:
            large_idx = right_idx

        if large_idx != ind:
            arr[ind], arr[large_idx] = arr[large_idx], arr[ind]
            self.heapifydown(arr, large_idx)

        return arr

    def changekey(self, arr, ind, val):
        if ind < 0 or ind >= self.cnt:
            return arr

        if arr[ind] > val:
            arr[ind] = val
            self.heapifydown(arr, ind)
        else:
            arr[ind] = val
            self.heapifyup(arr, ind)

        return arr

    def getmax(self):
        if self.cnt == 0:
            return None
        return self.arr[0]

    def isempty(self):
        return self.cnt == 0

    def getsize(self):
        return self.cnt

    def extractmax(self):
        if self.cnt == 0:
            return None

        max_val = self.arr[0]

        self.arr[0], self.arr[self.cnt - 1] = (
            self.arr[self.cnt - 1],
            self.arr[0]
        )

        self.arr.pop()
        self.cnt -= 1

        if self.cnt > 0:
            self.heapifydown(self.arr, 0)

        return max_val

    def insert(self, key):
        self.arr.append(key)
        self.cnt += 1
        self.heapifyup(self.arr, self.cnt - 1)

        return self.arr


def main():
    heap = Solution()

    heap.insert(10)
    heap.insert(20)
    heap.insert(30)
    heap.insert(60)
    heap.insert(40)
    heap.insert(70)

    print("Max Heap:", heap.arr)
    print("Maximum:", heap.getmax())
    print("Size:", heap.getsize())
    print("Is Empty:", heap.isempty())

    print("Extracted Maximum:", heap.extractmax())
    print("Heap after extraction:", heap.arr)

    heap.changekey(heap.arr, 0, 10)
    print("Heap after changing root to 10:", heap.arr)


if __name__ == '__main__':
    main()
