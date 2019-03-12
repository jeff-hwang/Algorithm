class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        cnt = 0

        while True:
            if 2 ** cnt == n:
                return True
            if 2 ** cnt > n : 
                return False
            cnt +=1

        return False


if __name__ == "__main__":
    input = 1
    sl = Solution().isPowerOfTwo(input)
    print(sl)
    