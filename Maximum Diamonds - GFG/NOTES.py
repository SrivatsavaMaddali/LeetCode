def maxDiamonds(self, A, N, K):
        dia=0
        for i in range(K):
            A.sort(reverse=True)
            dia=dia+A[0]
            A[0]=A[0]//2
        return dia
#This code passed 1110/1115 test cases. For the remaining 5, it exceeded time complexity.
