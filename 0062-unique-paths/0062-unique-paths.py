class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp=[[0]*n for _ in range(m)]
        for i in range(0,m):
            for j in range(0,n):
                if i==0 or j==0:
                    dp[i][j]=1
                else:
                    dp[i][j]=0
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j]=dp[i-1][j]+dp[i][j-1]    
        return dp[m-1][n-1]