class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        res=[]
        for i in range(len(nums)):
            if nums[i] not in res:
                res.append(nums[i])
        nums[:len(res)]=res
        for i in range(len(res),len(nums)):
            nums[i]='_'
        return len(res)