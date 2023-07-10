class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        i = 0
        j = k 
        maxi = 0
        if len(nums)==k:
            return round(sum(nums)/len(nums),5)
        n = len(nums)
        summ = maxi=sum(nums[:k])
        print(summ)
        while True:
            summ = summ + nums[j] - nums[i]
            print(summ)
            if summ > maxi:
                maxi = summ
            i += 1
            j += 1
            
            if j >= n:
                break
        
        return round(maxi / k, 5)
