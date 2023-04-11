class Solution:
    def longestPalindrome(self, s: str) -> str:
        s1 = ""  # Resulting String
        n = len(s)
        l = r = 0
        for i in range(n):
            # for checking Odd length palindrome
            l, r = i, i
            while l >= 0 and r < n and s[l] == s[r]:
                if (r - l + 1) > len(s1):
                    s1 = s[l:r + 1]  # taking the palindrome part
                l -= 1
                r += 1

            # for checking Even length palindrome
            l, r = i, i + 1
            while l >= 0 and r < n and s[l] == s[r]:
                if (r - l + 1) > len(s1):
                    s1 = s[l:r + 1]  # taking the palindrome part
                l -= 1
                r += 1

        return s1
