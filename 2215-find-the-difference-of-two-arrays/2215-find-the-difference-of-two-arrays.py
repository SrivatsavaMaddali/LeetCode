class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        result=[[],[]]
        for x in nums1:
            if x not in nums2 and x not in result[0]:
                result[0].append(x)
        for x in nums2:
            if x not in nums1 and x not in result[1]:
                result[1].append(x)
        return result
        