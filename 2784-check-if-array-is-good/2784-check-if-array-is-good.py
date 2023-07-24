class Solution:
    def isGood(self, nums: List[int]) -> bool:
        l = len(nums)
        d = {}
        for x in range(1,l):
            d[x] = 0
        for x in nums:
            if x>l-1:
                return False
            d[x] += 1
        print(d)
        if len(d)!=l-1:
            return False
        # if l==2:
        #     if nums!=[1,1]:
        #         return False
        for x in range(1, l - 1):
            if d[x]!= 1:
                return False
        if d[l - 1] != 2:
            return False
        return True
