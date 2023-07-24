​class Solution:
    def isGood(self, nums: List[int]) -> bool:
        l=len(nums)
        good=[]
        for i in range(1,l):
            good.append(i)
        good.append(l-1)
        return sorted(nums)==good
#Easier, intuitive approach
