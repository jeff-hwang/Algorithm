class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i, j = 0, 0
        while i+j < len(nums):
            if nums[i] == 0:
                nums.append(nums.pop(i))
                j += 1
            else:
                i += 1
        return nums

nums = [0,1,0,3,12]
sl = Solution()
print(sl.moveZeroes(nums))


