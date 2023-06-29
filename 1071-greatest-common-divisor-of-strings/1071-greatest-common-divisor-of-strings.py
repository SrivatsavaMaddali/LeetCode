import math
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        l1, l2 = len(str1), len(str2)
        gl = math.gcd(l1, l2)
        m = str1[:gl]
        if self.is_divisor(str1, m) and self.is_divisor(str2, m):
            return m
        return ""
    def is_divisor(self, s, d):
        return s == d * (len(s) // len(d))
