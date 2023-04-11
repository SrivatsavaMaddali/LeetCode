class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        new_list=nums1+nums2
        new_list.sort()
        n=len(new_list)
        if n % 2 == 0:
            med= (new_list[n // 2] + new_list[n // 2 - 1]) / 2
        else:
            med= new_list[n // 2]
        return med
        