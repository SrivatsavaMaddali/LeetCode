class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        indices = {}
        result=[]
        top=float(inf)
        for i in range(len(nums)):
            if i == 0 or nums[i] != nums[i-1]:
                if any(o < nums[i] for o in result):
                    if top!=nums[i]:
                        result.append(nums[i])
                    top=nums[i]
                else:
                    if nums[i] not in result:
                        result.append(nums[i])
        nums=result
        if len(nums)<3:
            return False
        if nums[::-1]==sorted(nums):
            return False
        if nums==sorted(nums):
            return True
        for i, num in enumerate(nums):
            if num in indices:
                indices[num].append(i)
            else:
                indices[num] = [i]
        temp = sorted(nums)
        for x in temp:
            for y in temp:
                for z in temp:
                    if x<y<z:
                        ones = indices[x]
                        twos = indices[y]
                        threes = indices[z]
                        if any(o < t < th for o in ones for t in twos for th in threes):
                            return True
        return False