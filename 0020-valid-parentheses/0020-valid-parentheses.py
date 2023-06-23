class Solution:
    def isValid(self, s: str) -> bool:
        norm=['(',')']
        sq=['[',']']
        cur=['{','}']
        flag=True
        op=['(','[','{']
        cl=[')',']','}']
        stak=[]
        st=[*s]
        opc=0
        clc=0
        for y in st:
            if y in  op:
                opc=opc+1
            elif y in cl:
                clc=clc+1
        if opc!=clc:
            return False
        if opc==0 or clc==0:
            return False
        for x in st:
            if x in op:
                stak.append(x)
            elif x in cl:
                if stak==[]:
                    return False
                top=stak.pop()
                if ((top in norm) and (x in norm)) or ((top in sq) and (x in sq)) or ((top in cur) and (x in cur)):
                    continue
                else:
                    flag=False
                    break
        return flag