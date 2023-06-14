#User function Template for python3
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

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N,K=map(int,input().split())
        A=list(map(int,input().split()))
        
        ob = Solution()
        print(ob.maxDiamonds(A,N,K))
# } Driver Code Ends