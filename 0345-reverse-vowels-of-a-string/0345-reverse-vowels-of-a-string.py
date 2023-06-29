class Solution:
    def reverseVowels(self, s: str) -> str:
        s=[*s]
        i=0
        j=len(s)-1
        vow = {'a','A','e','E','i','I','o','O','u','U'}
        while i<j:
            if s[i] in vow and s[j] in vow:
                s[i],s[j]=s[j],s[i]
                i+=1
                j-=1
            elif s[i] in vow and s[j] not in vow:
                j-=1
            elif s[i] not in vow and s[j] in vow:
                i+=1
            else:
                i+=1
                j-=1
        return "".join(s)