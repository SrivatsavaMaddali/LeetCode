#User function Template for python3
class Solution:

	def kLargest(self,arr, n, k):
		nums=[]
		for i in arr:
		    nums.append(i)
		nums.sort(reverse=True)
		return nums[0:k]


#{ 
 # Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, k = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.kLargest(arr, n, k)
        for x in ans:
            print(x, end=" ")
        print()
        tc -= 1

# } Driver Code Ends