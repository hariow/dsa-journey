## Kth Largest Element in an Array 


## Brute Force

import heapq

class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        ans=[]
        n=len(nums)

        for i in range(k):
            heapq.heappush(ans,nums[i]) 

        for i in range(k,n):
            if nums[i]>ans[0]:
                heapq.heappop(ans)
                heapq.heappush(ans,nums[i])

        return ans[0]       



## Optimal Solution but it getting TLE in Leetcode 

import random
class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        left,right = 0 , len(nums)-1
        
        while left <= right:
            pivotIndex=self.randomIndex(left,right)
            pivotIndex=self.partitionAndReturnIndex(nums,pivotIndex,left,right)

            if pivotIndex == k-1:
                return nums[pivotIndex]
            elif pivotIndex > k-1:
                right = pivotIndex -1
            else:
                left=pivotIndex + 1

    def randomIndex(self,left,right):
        return random.randint(left,right)
    
    def partitionAndReturnIndex(self,nums,pivotIndex,left,right):
        pivot=nums[pivotIndex]
        nums[left],nums[pivotIndex]=nums[pivotIndex],nums[left]
        ind = left+1

        for i in range(left+1,right+1):
            if nums[i]>pivot:
                nums[ind],nums[i]=nums[i],nums[ind]
                ind+=1
        
        ## Place the pivot at the correct index

        nums[left],nums[ind-1]=nums[ind-1],nums[left]
        return ind-1
    