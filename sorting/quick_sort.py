# Asceding Quick Sorting

def quick_sort(arr):

    if len(arr) <= 1:
        return arr

    pivot = arr[-1]

    left = []
    right = []

    for i in range(len(arr) - 1):
        if arr[i] <= pivot:
            left.append(arr[i])
        else:
            right.append(arr[i])

    left = quick_sort(left)
    right = quick_sort(right)

    return left + [pivot] + right


arr = [8, 4, 7, 9, 3, 10, 5]

print(quick_sort(arr))
