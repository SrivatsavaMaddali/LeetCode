class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        m=n
        n=abs(n)
        
        result=1
        while n>0:
            if n % 2 == 1:
                result *= x
            x *= x
            n //= 2
        return 1/result if m<0 else result
#This approach uses exponentiation, specifically, binary exponentiation
