class Solution:
    def addBinary(self, a: str, b: str) -> str:
        am=[*a]
        bm=[*b]
        am=[int(x) for x in am]
        bm=[int(y) for y in bm]
        am=am[::-1]
        bm=bm[::-1]
        an,bn=0,0
        for i in range(0,len(am)):
            an+=am[i]*(2**i)
        for i in range(0,len(bm)):
            bn+=bm[i]*(2**i)
        n=an+bn
        def DecimalToBinary(num):
            nonlocal l
            if num >= 1:
                DecimalToBinary(num // 2)
            l+=str(num%2)
        l=""
        DecimalToBinary(n)
        f=0
        for i in range(len(l)):
            if l[i]=='1':
                f=i
                break
        return l[f:]