
class Solution:
    def __init__(self):
        self.arr = []
        self.count = 0

    def heapifyUp(self, arr, ind):
        parentInd = (ind - 1) // 2

        if ind > 0 and arr[ind] < arr[parentInd]:
            arr[ind], arr[parentInd] = arr[parentInd], arr[ind]
            self.heapifyUp(arr, parentInd)

    def heapifDown(self, arr, ind):
        n = len(arr)
        smallestInd = ind

        leftChildInd = 2 * ind + 1
        rightChildInd = 2 * ind + 2

        if leftChildInd < n and arr[leftChildInd] < arr[smallestInd]:
            smallestInd = leftChildInd

        if rightChildInd < n and arr[rightChildInd] < arr[smallestInd]:
            smallestInd = rightChildInd

        if smallestInd != ind:
            arr[smallestInd], arr[ind] = arr[ind], arr[smallestInd]
            self.heapifDown(arr, smallestInd)

    def initialize(self):
        self.arr.clear()
        self.count = 0

    def insert(self, key):
        self.arr.append(key)
        self.heapifyUp(self.arr, self.count)
        self.count += 1

    def changeKey(self, index, new_val):
        if index < 0 or index >= self.count:
            return

        if self.arr[index] > new_val:
            self.arr[index] = new_val
            self.heapifyUp(self.arr, index)
        else:
            self.arr[index] = new_val
            self.heapifDown(self.arr, index)

    def extractMin(self):
        if self.count == 0:
            return None

        ele = self.arr[0]

        self.arr[0], self.arr[self.count - 1] = self.arr[self.count - 1], self.arr[0]
        self.arr.pop()
        self.count -= 1

        if self.count > 0:
            self.heapifDown(self.arr, 0)

        return ele

    def isEmpty(self):
        return self.count == 0

    def getMin(self):
        return self.arr[0] if self.count > 0 else None

    def heapSize(self):
        return self.count


def main():
    heap = Solution()
    heap.initialize()

    heap.insert(4)
    heap.insert(5)
    heap.insert(10)

    print(f"Min = {heap.getMin()}")
    print(f"Size = {heap.heapSize()}")
    print(f"Is Empty = {heap.isEmpty()}")

    print("Extracting min")
    print(heap.extractMin())

    print("Changing index 0 to 10")
    heap.changeKey(0, 10)

    print(f"Min = {heap.getMin()}")


if __name__ == "__main__":
    main()
