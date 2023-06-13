class Solution:
    def myAtoi(self, s: str) -> int:
        indi=[*s]
        if s=="" or s==" " or s=="  ":
            return 0
        lower=-2147483648
        upper=2147483647
        final=0
        posflag=1
        negflag=1
        nums=['0','1','2','3','4','5','6','7','8','9','-','+']
        num=['0','1','2','3','4','5','6','7','8','9']
        result=[]
        if indi[0] not in nums:
            if indi[0]!=' ':
                return 0
        print(indi)
        for x in indi:
            if x=='.':
                break
            if len(result)!=0 and x not in num:
                break
            if len(result)==0 and x not in nums and x!=' ':
                return 0
            if x in nums:
                result.append(x)
        print(result)
        if not result:
            return 0
        signs=['-','+']
        c=0
        for x in result:
            if x in signs:
                c+=1
        if c==1 and result[0] not in signs:
            return 0
        if c>1:
            return 0
        if result[0]=='-':
            negflag=-1
            result.pop(0)
        elif result[0]=='+':
            posflag=1
            result.pop(0)   
        else:
            posflag=1
        
        for y in result[0:len(result)]:
            final=final*10+int(y)
        final=final*negflag
        if final>=lower and final<=upper:
            return final
        elif final<lower:
            return lower
        elif final>upper:
            return upper
        else:
            return 0