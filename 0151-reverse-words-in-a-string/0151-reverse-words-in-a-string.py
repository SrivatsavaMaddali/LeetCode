class Solution:
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
        if wc==0:
            words.append(s[start:len(s)])
        else:
            words.append(s[start+1:len(s)])
        print(words)
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
                
        