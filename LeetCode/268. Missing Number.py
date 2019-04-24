class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # case 1
        '''
        dic = {}
        for i in nums:
            dic[i] = True
        
        ln = len(nums)
        
        for i in range(ln+1):
            try:
                if dic[i] == True:
                    pass
            except:
                return i
        '''
        # case 2
        return sum(x for x in range(0, len(nums)+1)) - sum(nums)


if __name__=="__main__":
    nums = [3,0,1]
    sl = Solution().missingNumber(nums)
    print(sl)