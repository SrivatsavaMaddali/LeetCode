import math
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        gl = math.gcd(len(str1), len(str2))
        m = str1[:gl]
        if str1==m*(len(str1)//gl) and str2==m*(len(str2)//gl):
                return m
        return ""
