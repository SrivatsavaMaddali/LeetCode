class Solution:
    def maxArea(self, height: List[int]) -> int:
        i=0
        j=len(height)-1
        maxi=0
        while i<j:
            if height[i]<height[j]:
                water=(j-i)*height[i]
                i=i+1
            else:
                water=(j-i)*height[j]
                j=j-1
            if water>maxi:
                maxi=water
        return maxi
        