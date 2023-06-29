class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result=[]
        m=max(candies)
        for i in candies:
            result.append(True if extraCandies+i>=m else False)
        return result
        