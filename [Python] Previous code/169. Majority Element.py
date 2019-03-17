class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        
        # 원소들 중 가장 많이 나오는 원소를 반환하시오
        test data
        Input: [3,2,3]
        Output: 3

        Input: [2,2,1,1,1,2,2]
        Output: 2
        """
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        return candidate

nums = [1,1,2,3,1]
sl = Solution()
print(sl.majorityElement(nums))
        
        