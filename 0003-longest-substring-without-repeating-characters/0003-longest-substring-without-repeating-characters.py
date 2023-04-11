class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n=len(s)
        if n==0:
            return 0
        maxi=1
        for i in range(0,n):
            final=[]
            news=s[i:n]
            for j in news:
                if j not in final:
                    final.append(j)
                else:
                    break
            maxi=max(maxi,len(final))
        return maxi