class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        return sum(nums) - len(nums)*min(nums)

if __name__ == "__main__":
    inData = [1,2,3]
    print(Solution().minMoves(inData))