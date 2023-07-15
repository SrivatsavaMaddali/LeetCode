class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        if nums[len(nums)-1]<target:
            return len(nums)
        if nums[0]>target:
            return 0
        nums.append(target)
        nums.sort()
        return nums.index(target)