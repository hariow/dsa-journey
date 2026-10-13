class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        result=[]
        max_candies = max(candies)

        for i in range(len(candies)):
       

            if candies[i] + extraCandies >= max_candies:
                result.append(True)
            else:
                result.append(False)
        
        return result
