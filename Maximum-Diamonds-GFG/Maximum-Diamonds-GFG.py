import heapq
class Solution:
    def maxDiamonds(self, A, N, K):
        dia = 0
        max_heap = [-num for num in A]
        heapq.heapify(max_heap)

        for i in range(K):
            max_element = -heapq.heappop(max_heap)
            dia += max_element
            heapq.heappush(max_heap, -(max_element // 2))

        return dia
