class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        if mat==target:
            return True
        for k in range(3):
            n=len(mat[0])
            for i in range(n):
                t=mat[i]
                for j in range(n):
                    mat[j].append(t[j])
            for i in range(n):
                for j in range(n):
                    mat[i].pop(0)
                mat[i]=mat[i][:-n-1:-1]
            if mat==target:
                return True
        return False