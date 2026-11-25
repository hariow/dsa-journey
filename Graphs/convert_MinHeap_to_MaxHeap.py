## Convert Min Heap to Max Heap


class Solution:
    def heapify_down(self, arr, ind, n):
        while True:
            largest = ind
            left = 2 * ind + 1
            right = 2 * ind + 2

            if left < n and arr[left] > arr[largest]:
                largest = left

            if right < n and arr[right] > arr[largest]:
                largest = right

            if largest == ind:
                break

            arr[ind], arr[largest] = arr[largest], arr[ind]
            ind = largest

    def minToMaxHeap(self, arr):
        n = len(arr)

        for ind in range(n // 2 - 1, -1, -1):
            self.heapify_down(arr, ind, n)

        return arr
