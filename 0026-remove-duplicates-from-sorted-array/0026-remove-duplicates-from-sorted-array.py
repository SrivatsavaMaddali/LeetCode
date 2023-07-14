class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        res=[]
        n=len(nums)
        for i in range(n):
            if nums[i] not in res:
                res.append(nums[i])
        k=len(res)
        nums[:k]=res
        return k