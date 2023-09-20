class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n=len(matrix[0])
        for i in range(n):
            t=matrix[i]
            for j in range(n):
                matrix[j].append(t[j])
        for i in range(n):
            for j in range(n):
                matrix[i].pop(0)
            matrix[i]=matrix[i][:-n-1:-1]
# class Solution:
#     def rotate(self, matrix: List[List[int]]) -> None:
#         """
#         Do not return anything, modify matrix in-place instead.
#         """
#         n = len(matrix[0])
        
#         # Transpose the matrix
#         for i in range(n):
#             for j in range(i, n):
#                 matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
#         # Reverse each row
#         for i in range(n):
#             matrix[i] = matrix[i][::-1]            
            
            

