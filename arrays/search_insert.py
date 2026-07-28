# Search Insert Position

nums = [1,2,3,4,5,7,8,9]

def search_pos(nums):
    n = len(nums)
    target = 6
    low = 0
    high = n - 1

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] == target:
            return mid

        elif nums[mid] > target:
            high = mid - 1

        else:
            low = mid + 1

    return low

print(search_pos(nums))