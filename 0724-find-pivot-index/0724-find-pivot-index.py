class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            leftsum= 0 if i==0 else sum(nums[:i])
            rightsum=0 if i==len(nums)-1 else sum(nums[i+1:])
            if leftsum==rightsum:
                return i
        return -1