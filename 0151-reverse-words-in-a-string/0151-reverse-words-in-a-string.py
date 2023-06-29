class Solution:
    def reverseWords(self, s: str) -> str:
        words=s.split()
        result=""
        for x in words[::-1]:
            result+=x+" "
        result=result.strip()
        return result
                
        