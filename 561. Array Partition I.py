class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        nums.sort()
        # nums 의 길이를 구하여 n을 구함
        numsLen = len(nums)
        
        # n 을 구함
        n = numsLen / 2

        # 결과값을 받을 변수
        res = 0
        
        # nums의 index를 짝수 인덱스만 뽑아 res에 더함
        for i in range(0, numsLen, 2):
           res += nums[i]
           
        return res 





nums = [1,4,3,2]
Solution().arrayPairSum(nums)