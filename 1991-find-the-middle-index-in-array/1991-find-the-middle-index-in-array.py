class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        wholesum=sum(nums)
        for i in range(len(nums)):
            leftsum= sum(nums[:i])
            rightsum=wholesum-leftsum-nums[i]
            if leftsum==rightsum:
                return i
        return -1