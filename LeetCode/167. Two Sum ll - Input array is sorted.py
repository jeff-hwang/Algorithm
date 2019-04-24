class Solution(object):
    def twoSum(self, nums, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        # 문제설명
        # 오름차순으로 정렬된 배열이 있다
        # numbers의 원소 2개를 중복되지 않게 골라 더한 값이
        # target 일 때 원소의 index를 list로 return 하라
        # 단, index는 1부터 시작한다.
        
        '''
        초기 접근법
        단순하게 2중 for 문을 돌리면 될 것이라 생각을 하였다.
        '''

        ln = len(nums)
        for i in range(ln-1):
            for j in range(i+1, ln):
                if nums[i]+nums[j] == target:
                    return [i+1, j+1]

        # 하지만 time limit 에 걸리게 된다.
        # 별의 별 생각을 다하고 이것 저것 다 해보아도 안되어
        # Discuss 에서 다른 사람이 작성한 코드를 보고 새로운 사고 방식을 보았다.

        

        # nums 의 배열의 길이를 저장
        ln = len(nums)
        
        # 배열의 left index
        left = 0
        # 배열의 right index
        right = ln - 1
        
        # left index 가 right 보다 작을 때 까지 while문을 돌린다.
        while left < right:
            # nums[left] +nums[right] 가 target 보다 크면
            # right index를 하나 감소시킨다.
            if nums[left] + nums[right] > target:
                right -= 1
            # nums[left] + nums[right] < target 보다 작으면
            # left index 를 증가시킨다.
            elif nums[left] + nums[right] < target:
                left += 1
            # 만약 nums[left] + nums[right] 가 target 가 일치한다면
            # index+1 씩해서 return 한다.
            elif nums[left] + nums[right] == target:
                return [left + 1, right + 1]
                
        return [left + 1, right + 1]

        
if __name__ == '__main__':
    numbers = [2, 7, 11, 15]
    target = 9

    sl = Solution().twoSum(numbers, target)
    print(sl)