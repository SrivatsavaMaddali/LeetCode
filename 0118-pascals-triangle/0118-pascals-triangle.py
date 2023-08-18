class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        fin=[]
        fin.append([1])
        fin.append([1,1])
        l=len(fin)
        while l<numRows:
            fin.append([])
            fin[-1].append(1)
            for i in range(len(fin[-2])-1):
                fin[-1].append(fin[-2][i]+fin[-2][i+1])
            fin[-1].append(1)
            l+=1
        return fin[:numRows]