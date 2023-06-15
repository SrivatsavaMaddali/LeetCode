#User function Template for python3

class Solution:
    def longestPalin(self, S):
        if not S:
            return ""

        longest = ""
        n = len(S)

        for i in range(n):
            # Check for odd-length palindromes
            l, r = i, i
            while l >= 0 and r < n and S[l] == S[r]:
                l -= 1
                r += 1

            odd_palindrome = S[l+1:r]

            # Check for even-length palindromes
            l, r = i, i+1
            while l >= 0 and r < n and S[l] == S[r]:
                l -= 1
                r += 1

            even_palindrome = S[l+1:r]

            # Update longest palindrome if necessary
            if len(odd_palindrome) > len(longest):
                longest = odd_palindrome
            if len(even_palindrome) > len(longest):
                longest = even_palindrome

        return longest

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        S = input()

        ob = Solution()

        ans = ob.longestPalin(S)

        print(ans)
# } Driver Code Ends