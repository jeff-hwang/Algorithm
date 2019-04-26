class Solution(object):
    def bitwiseComplement(self, N):
        """
        :type N: int
        :rtype: int
        """
        bin = ""
        while N > 0 :
            bin += str(N % 2)
            N //= 2

        #print(bin)
        
        #bin = reversed(bin)
        res = ""
        
        
        for i in bin:
            if i == "1":
                res += "0"

            else:
                res += "1"
        #print(res)
        rst = 0
        for i, v in enumerate(res):
            if v=="0":
                pass
            else:
                rst += (2**i)
        
        return rst
        
        

if __name__ == "__main__":
    sl = Solution().bitwiseComplement(5)
    print(sl)
    