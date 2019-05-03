class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        return a+b

if __name__ =='__main__':
    a = -2
    b = 3
    sl = Solution().getSum(a, b)
    print(sl)