## check array represents in a Max Heap



class Solution:
    def isMaxHeap(self, arr):
        n = len(arr)

        for ind in range(n // 2 - 1, -1, -1):
            leftChild = 2 * ind + 1
            rightChild = 2 * ind + 2

            if leftChild < n and arr[leftChild] > arr[ind]:
                return False

            if rightChild < n and arr[rightChild] > arr[ind]:
                return False

        return True


def main():
    arr = [70, 40, 60, 10, 30, 20]

    obj = Solution()

    if obj.isMaxHeap(arr):
        print("Valid Max Heap")
    else:
        print("Not a Max Heap")


if __name__ == "__main__":
    main()
