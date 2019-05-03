class Solution(object):
    dic = {}
    obstacleGrid = None

    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        self.obstacleGrid = obstacleGrid

        return self.calcPath(m, n, self.dic)

    def calcPath(self, m, n, dic):

        if (m, n) in self.dic:
            return dic[(m, n)]

        if self.obstacleGrid[m-1][n-1] == 1:
            self.dic[(m, n)] = 0
            return 0

        if m == 1 and n == 1:
            self.dic[(1, 1)] = 1
            return 1
        if m == 1:
            if 1 in self.obstacleGrid[0]:
                for i in range(self.obstacleGrid[0].index(1)+1, n+1):
                    self.dic[(1, i)] = 0
                return 0
            else:
                for i in range(self.obstacleGrid[0].index(1)+1, n+1):
                    self.dic[(1, i)] = 1
                return 1
        if n == 1:
            if 1 in self.obstacleGrid[0]:
                for i in range(self.obstacleGrid[0].index(1)+1, n+1):
                    self.dic[(1, i)] = 0
                return 0
            else:
                for i in range(self.obstacleGrid[0].index(1)+1, n+1):
                    self.dic[(1, i)] = 1
                return 1

        self.dic[m, n] = self.calcPath(
            m-1, n, self.dic) + self.calcPath(m, n-1, self.dic)
        return self.dic[m, n]


if __name__ == "__main__":
    sl = Solution()
    print(sl.uniquePathsWithObstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]]))
