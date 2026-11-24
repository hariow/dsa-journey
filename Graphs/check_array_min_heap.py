## check array represents in a Min Heap


class Solution:
    def isMinHeap(self, arr):
        n = len(arr)

        for ind in range(n // 2 - 1, -1, -1):
            leftChild = 2 * ind + 1
            rightChild = 2 * ind + 2

            if leftChild < n and arr[leftChild] < arr[ind]:
                return False

            if rightChild < n and arr[rightChild] < arr[ind]:
                return False

        return True


def main():
    arr = [10, 20, 15, 30, 40]

    obj = Solution()

    if obj.isMinHeap(arr):
        print("Valid Min Heap")
    else:
        print("Not a Min Heap")


if __name__ == "__main__":
    main()
