class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        w1 = [*word1]
        w2 = [*word2]
        result = ""
        n = min(len(w1), len(w2))

        for i in range(n):
            result += w1[i] + w2[i]

        result += ''.join(w1[n:]) + ''.join(w2[n:])
        return result