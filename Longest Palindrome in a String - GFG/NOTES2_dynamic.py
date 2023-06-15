def longestPalin(self, S):
    n = len(S)
    longest = ""
    dp = [[False] * n for _ in range(n)]

    # All individual characters are palindromes of length 1
    for i in range(n):
        dp[i][i] = True
        longest = S[i]

    # Check for palindromes of length 2
    for i in range(n - 1):
        if S[i] == S[i + 1]:
            dp[i][i + 1] = True
            longest = S[i:i + 2]

    # Check for palindromes of length greater than 2
    for length in range(3, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if S[i] == S[j] and dp[i + 1][j - 1]:
                dp[i][j] = True
                longest = S[i:j + 1]

    return longest
