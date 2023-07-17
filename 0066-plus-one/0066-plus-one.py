class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n=len(digits)
        if n==1:
            if digits[0]<9:
                digits[0]+=1
            elif digits[0]==9:
                digits[0]=1
                digits.append(0)
            return digits   
        if digits[n-1]<9:
            digits[n-1]+=1
        elif digits[n-1]==9:
            digits[n-1]=0
            digits[:n-1]=self.plusOne(digits[:n-1])
        return digits