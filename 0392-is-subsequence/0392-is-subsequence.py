class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s=[*s]
        t=[*t]
        i=0
        j=0
        cnt=0
        while i<len(s) and j<len(t):
            if s[i]==t[j]:
                i+=1
                j+=1
                cnt+=1
                continue
            if t[j]!=s[i]:
                j+=1
        return cnt==len(s)