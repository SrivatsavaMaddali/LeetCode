class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.r,self.x,self.y=radius,x_center,y_center
    def randPoint(self) -> List[float]:
        r = sqrt(random.random())*self.r
        theta=random.uniform(0, 2*pi)
        return [self.x + r * math.cos(theta), self.y + r *math.sin(theta)]
# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()