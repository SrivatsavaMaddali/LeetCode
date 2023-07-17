class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        temp=[]
        for x in nums:
            if x!=val:
                temp.append(x)
        nums[:len(temp)]=temp
        return len(temp)