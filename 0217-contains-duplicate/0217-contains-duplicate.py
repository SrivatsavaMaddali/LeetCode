class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # n=len(nums)
        # for i in range(0,n):
        #     if nums[i] in nums[i+1:n]:
        #         return True
        # return False
        # Exceeds time limit
        
        # temp=[]
        # for x in nums:
        #     if x not in temp:
        #         temp.append(x)
        # if len(temp)==len(nums):
        #     return False
        # else:
        #     return True
        # Exceeds time limit
        
        # temp=[]
        # for x in nums:
        #     if x not in temp:
        #         temp.append(x)
        #     else:
        #         return True
        # return False
        # Exceeds time limit
        
        # temp=[]
        # nums.sort()
        # for x in nums:
        #     if x in temp:
        #         return True
        #     else:
        #         temp.append(x)
        # return False
        # Exceeds time limit
    
        # temp=set()
        # for x in nums:
        #     if x in temp:
        #         return True
        #     else:
        #         temp.add(x)
        # return False
        
        temp=set(nums)
        if len(temp)==len(nums):
            return False
        return True
        
        
        