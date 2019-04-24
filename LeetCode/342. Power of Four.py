class Solution(object):
    def isPowerOfFour(self, num):

        while num>4 :
            if num % 4 != 0:
                return False

            num /= 4
            
        return num in (1, 4)
        

if __name__ == "__main__":
    sl = Solution().isPowerOfFour(64)
    print(sl)