class Solution(object):
    dic = {}

    def uniquePaths(self, m, n):

        if (m, n) in self.dic:
            return self.dic[(m, n)]
        if m == 1 and n == 1:
            self.dic[(m, n)] = 1
            return 1
        if m == 1 or n == 1:
            self.dic[(m, n)] = 1
            return 1

        self.dic[(m, n)] = self.uniquePaths(m-1, n) + self.uniquePaths(m, n-1)
        return self.dic[(m, n)]


if __name__ == "__main__":
    sl = Solution()
    print(sl.uniquePaths(120, 120))
    print(sl.dic)
