## Heap Sort Algorithm


def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heap_sort(arr):
    n = len(arr)

    # Build max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements from heap one by one
    for last_index in range(n - 1, 0, -1):
        arr[0], arr[last_index] = arr[last_index], arr[0]
        heapify(arr, last_index, 0)

    return arr


# Example
arr = [4, 10, 3, 5, 1]

heap_sort(arr)
print(arr)
