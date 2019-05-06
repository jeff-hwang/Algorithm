class Solution(object):
    def numJewelsInStones(self, J, S):
        li  = list(set([i for i in J]))
        cnt = 0
        
        for i in S:
            if i in li:
                cnt += 1
        
        return cnt
            

if __name__ == "__main__":
    J = "aA"
    S = "aAAbbbb"
    sl = Solution().numJewelsInStones(J, S)
    print(sl)