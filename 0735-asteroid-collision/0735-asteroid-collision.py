class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        result=[]
        for x in asteroids:
            while result and x < 0 < result[-1]:
                if result[-1]<-x:
                    result.pop()
                    continue
                elif result[-1]==-x:
                    result.pop()
                break
            else:
                result.append(x)
        return result