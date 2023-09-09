class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        dot=queryIP.count('.')
        col=queryIP.count(':')
        hexa="0123456789abcdefABCDEF"
        if dot==3:
            ind=queryIP.split(".")
            for x in ind:
                if x.isnumeric()==False:
                    return "Neither"
                if len(x) in range(1,4):
                    if len(x)==3 and (x.count('0')==3 or x[0]=='0'):
                        return "Neither"
                    elif len(x)==2 and (x[0]=='0' or x.count('0')==2):
                        return "Neither"
                else:
                        return "Neither"
                if int(x) not in range(0,256):
                    return "Neither"
            return "IPv4"
        elif col==7:
            ind=queryIP.split(":")
            for x in ind:
                if x.isalnum():
                    if len(x) in range(1,5):
                        y=all(c in hexa for c in x)
                        if y==False:
                            return "Neither"
                    else:
                        return "Neither"
                else:
                    return "Neither"
            return "IPv6"
        else:
            return "Neither"