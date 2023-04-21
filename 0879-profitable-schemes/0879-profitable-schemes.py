class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        # Initialize variables
        MOD = 10**9 + 7
        dp = [[[0] * (n + 1) for _ in range(minProfit + 1)] for _ in range(len(group) + 1)]
        dp[0][0][0] = 1

        for i in range(1, len(group) + 1):
            for p in range(minProfit + 1):
                for g in range(n + 1):
                    dp[i][p][g] = dp[i - 1][p][g] 
                    if g >= group[i - 1]:
                        dp[i][p][g] += dp[i - 1][max(0, p - profit[i - 1])][g - group[i - 1]]
                        dp[i][p][g] %= MOD

        total_schemes = 0
        for g in range(n + 1):
            total_schemes += dp[len(group)][minProfit][g]
            total_schemes %= MOD

        return total_schemes
