class Solution(object):
    lst = [None] * 31

    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N == 0:
            self.lst[0] = 0
            return 0

        if N == 1:
            self.lst[1] = 1
            return 1

        if self.lst[N] != None:
            return self.lst[N]

        self.lst[N] = self.fib(N-1) + self.fib(N-2)
        return self.lst[N]
