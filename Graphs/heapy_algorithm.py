# Heapify Algorithm

class Solution:
    def heapify_down(self, arr, ind):
        n = len(arr)
        largest_ind = ind

        leftChildInd = 2 * ind + 1
        rightChildInd = 2 * ind + 2

        if leftChildInd < n and arr[leftChildInd] > arr[largest_ind]:
            largest_ind = leftChildInd

        if rightChildInd < n and arr[rightChildInd] > arr[largest_ind]:
            largest_ind = rightChildInd

        if largest_ind != ind:
            arr[largest_ind], arr[ind] = arr[ind], arr[largest_ind]
            self.heapify_down(arr, largest_ind)

    def heapify_up(self, arr, ind):
        parent_ind = (ind - 1) // 2

        if ind > 0 and arr[ind] > arr[parent_ind]:
            arr[ind], arr[parent_ind] = arr[parent_ind], arr[ind]
            self.heapify_up(arr, parent_ind)
    
    def heapify(self, arr, ind, val):
        oldVal = arr[ind]
        arr[ind] = val

        if val > oldVal:
            self.heapify_up(arr, ind)
        elif val < oldVal:
            self.heapify_down(arr, ind)

        return arr

sol = Solution()
arr = [10, 7, 6, 4, 5, 4, 5, 3, 2]
ind = 0
val = 1
print(sol.heapify(arr, ind, val))