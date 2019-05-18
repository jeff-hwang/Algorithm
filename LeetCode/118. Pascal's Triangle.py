class Solution(object):
    def generate(self, numRows):
        tri = []
        tri.append([1])
        tri.append([1,1])
        if numRows < 3:
            return tri[0:numRows]
        for i in range(2, numRows):
            cache = [1]
            for j in range(1, i):
                cache.append(tri[i-1][j-1]+tri[i-1][j])
            cache.append(1)
            tri.append(cache)
        return tri

sl = Solution()
print(sl.generate(5))