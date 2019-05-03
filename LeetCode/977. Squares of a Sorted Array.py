class Solution(object):
    def sortedSquares(self, A):
        res = [self.calcArea(i) for i in A]
        return sorted(res)
        
    def calcArea(self, x):
        return x**2