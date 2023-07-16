class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        wholesum=sum(nums)
        for i in range(len(nums)):
            leftsum= 0 if i==0 else sum(nums[:i])
            rightsum=wholesum-leftsum-nums[i]
            if leftsum==rightsum:
                return i
        return -1