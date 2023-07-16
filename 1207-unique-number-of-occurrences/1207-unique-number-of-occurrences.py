class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        Sat={}
        for i in arr:
            if i in Sat:
                Sat[i]=Sat[i]+1
            else:
                Sat[i]=0
        counts=Sat.values()
        return True if len(counts)==len(set(counts)) else False