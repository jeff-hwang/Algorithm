class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        ln = len(nums)
        mx = sum(nums[0:0+k])
        preMx = mx
        if k == 1:
            return max(nums)

        for i in range(1, ln - k+1):

            preMx = preMx - nums[i-1]+nums[i+k-1]
            mx = max(preMx, mx)

        return mx/float(k)


if __name__ == "__main__":
    sl = Solution().findMaxAverage([4, 2, 1, 3, 3], 2)
    print(sl)
