class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s=[*s]
        t=[*t]
        if len(s)>len(t):
            return False
        if len(s)==len(t) and s!=t:
            return False
        if len(s)==1 and s[0] in t:
            return True
        i,j=0,0
        while i<len(s) and j<len(t):
            if t[j]==s[i]:
                i+=1
            j+=1
        return i==len(s)