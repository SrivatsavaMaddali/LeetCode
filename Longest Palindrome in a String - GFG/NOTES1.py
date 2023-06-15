def longestPalin(self, S):
        # code here
        maxi=[]
        stri=[]
        reve=[]
        maxi=S[0]
        # print(maxi)
        for j in range(len(S)+1):
            for i in range(j+1,len(S)+1):
                stri=S[j:i+1]
                # print("str:"+str)
                reve=stri[::-1]
                if stri==reve:
                    if len(stri)>len(maxi):
                        maxi=stri

        return maxi
#O(n*n*n) time complexity
