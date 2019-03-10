class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        '''
        fact = self.factorial(n)
        
        ln = len(str(fact))
        
        lst = list(str(fact))
        rst = 0
        
        for i in range(ln-1, -1, -1):
            if lst[i] == '0':
                rst += 1
            else :
                break
        
        return rst

        '''
        cnt = 0
        while n >= 5:
            n //= 5
            cnt += n
        return cnt
        
    
    def factorial(self, n):
        if n==0:
            return 1
        else:
            return n * self.factorial(n-1)


'''
if __name__ == "__main__":
    n = 3
    sl = Solution().trailingZeroes(n)
    print(sl)
'''