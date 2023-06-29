import math
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        l1, l2 = len(str1), len(str2)
        gl = math.gcd(l1, l2)
        m = str1[:gl]
        if str1==m*(len(str1)//len(m)):
            if str2==m*(len(str2)//len(m)):
                return m
        return ""
