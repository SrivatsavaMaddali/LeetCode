class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod=1
        cnt=0
        prod0=1
        for i in range(len(nums)):
            prod=prod*nums[i]
            if nums[i]!=0:
                prod0=prod0*nums[i]
            if nums[i]==0:
                cnt=cnt+1
        if cnt>1:
            return [0 for x in nums]
        result=[]
        for x in nums:
            if cnt==1 and x==0:
                result.append(prod0)
            else:
                result.append(int(prod/x))
        return result