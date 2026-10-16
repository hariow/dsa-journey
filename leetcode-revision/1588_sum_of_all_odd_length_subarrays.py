class Solution:
    def sumOddLengthSubarrays(self, arr: list[int]) -> int:
        total = 0

        for i in range(len(arr)):
            subarray_sum = 0

            for j in range(i , len(arr)):
                subarray_sum+=(arr[j])

                if (j - i + 1) % 2 !=0:
                    total+=subarray_sum

        return total

        