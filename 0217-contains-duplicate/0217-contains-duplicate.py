class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        temp=set(nums)
        return False if len(temp)==len(nums) else True
        
        
        