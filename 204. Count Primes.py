class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        '''
        cnt = 0
        lst = []
        for i in range(2, n):
            less = 0
            if i> 11 and (i % 2 == 0 or i % 3 == 0 or i % 5 == 0 or \
                i % 7 or i % 11):
                pass
            for j in range(2, i):
                if i % j == 0:
                    less+=1
                if less > 0:
                    break
            if less == 0:
                cnt +=1
        '''
        cnt = 0
        lst = [2, 3, 5, 7]
        if n < 10 :
            for i in lst :
                if i < n :
                    cnt +=1
                else :
                    return cnt
            return cnt
        
        for i in range(10, n):
            if i%2==0 or i%3==0 or i%5==0 or i%7 == 0:
               pass
            else:
                cnt+=1
        return cnt+4

if __name__ == "__main__":
    n = 10
    sl = Solution().countPrimes(499979)
    print(sl)