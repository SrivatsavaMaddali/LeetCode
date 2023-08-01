ALLOF THESE EXCEED TIME LIMIT FOR LARGE ARRAYS
        
        n=len(nums)
        for i in range(0,n):
            if nums[i] in nums[i+1:n]:
                return True
        return False
-------------------------------------------------------------------------------------------        
        temp=[]
        for x in nums:
            if x not in temp:
                temp.append(x)
        if len(temp)==len(nums):
            return False
        else:
            return True
-------------------------------------------------------------------------------------------           
        temp=[]
        for x in nums:
            if x not in temp:
                temp.append(x)
            else:
                return True
        return False
-------------------------------------------------------------------------------------------           
        temp=[]
        nums.sort()
        for x in nums:
            if x in temp:
                return True
            else:
                temp.append(x)
        return False
