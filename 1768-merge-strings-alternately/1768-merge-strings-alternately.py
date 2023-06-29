# class Solution:
#     def mergeAlternately(self, word1: str, word2: str) -> str:
#         w1 = [*word1]
#         w2 = [*word2]
#         result = ""
#         n = min(len(w1), len(w2))

#         for i in range(n):
#             result += w1[i] + w2[i]

#         result += ''.join(w1[n:]) + ''.join(w2[n:])
#         return result
class Solution(object):
    def mergeAlternately(self, word1, word2):
        m = len(word1)
        n = len(word2)
        i = 0
        j = 0
        result = []

        while i < m or j < n:
            if i < m:
                result += word1[i]
                i += 1
            if j < n:
                result += word2[j]
                j += 1

        return "".join(result)