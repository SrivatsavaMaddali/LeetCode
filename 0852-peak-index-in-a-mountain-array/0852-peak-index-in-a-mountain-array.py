class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        maxi,i=0,0
        while i<len(arr):
            if arr[i]>arr[maxi]:
                maxi=i
            i+=1
        return maxi