class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m=len(matrix)
        n=len(matrix[0])
        # rs=[1 for _ in range(m)]
        # cs=[1 for _ in range(n)]
        # for i in range(m):
        #     for j in range(n):
        #         if matrix[i][j]==0 and (rs[i]==1 and cs[j]==1):
        #             rs[i]=0
        #             cs[j]=0
        #             matrix[i]=[0 for _ in range(n)]
        #             for k in range(m):
        #                 matrix[k][j]=0
        rs=[]
        cs=[]
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    rs.append(i)
                    cs.append(j)
        for x in rs:
            matrix[x]=[0 for _ in range(n)]
        for y in cs:
            for p in range(m):
                matrix[p][y]=0
        
                    