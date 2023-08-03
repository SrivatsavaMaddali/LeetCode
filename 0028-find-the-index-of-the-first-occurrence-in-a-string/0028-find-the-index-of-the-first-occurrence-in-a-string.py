class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i,j=0,0
        m,n=len(haystack),len(needle)
        while i<m and j<n:
            if haystack[i]==needle[j]:
                i+=1
                j+=1
            else:
                i=i-j+1
                j=0
        return i-n if j==n else -1