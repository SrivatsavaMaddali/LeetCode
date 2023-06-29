​class Solution:
    def reverseWords(self, s: str) -> str:
        s.strip()
        words=[]
        start=0
        wc=0
        for i in range(len(s)):
            if s[i]==' ':
                wc+=1
                words.append(s[start:i].strip())
                start=i
        words.append(s[start:len(s)] if wc==0 else s[start+1:len(s)])
        nice=[]
        for y in words:
            if y!='':
                nice.append(y)
        words=nice
        result=""
        for x in words[::-1]:
            result+=x+" "
        result=result.strip()
        return result
#Another solution. This one doesn't use split()
