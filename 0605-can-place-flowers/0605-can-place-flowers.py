class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        i=0
        if n==0:
            return True
        # if n>ceil(len(flowerbed)/2):
        #     return False
        # if len(flowerbed) == 1:
        #     return True if n==1 and flowerbed[0] == 0 else False
        # if len(flowerbed) == 1:
        #     return True if n==0 and flowerbed[0] == 1 else False
        # if len(flowerbed) == 2:
        #     return True if flowerbed== [0,0] else False
        cnt=0
        for i in range(len(flowerbed)):
            if flowerbed[i]==0 and (i==0 or flowerbed[i-1]!=1) and (i==len(flowerbed)-1 or flowerbed[i+1]!=1):
                cnt+=1
                flowerbed[i]=1
        if cnt>=n:
            return True
        else:
            return False

