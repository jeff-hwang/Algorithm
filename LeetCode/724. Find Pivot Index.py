class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # array nums의 원소들의 합
        sumNums = sum(nums)
        # 왼쪽의 합을 저장한 변수
        sumLeft = 0

        # nums를 index 와 value를 반복문을 돌린다.
        for i, val in enumerate(nums):
            # 왼쪽의 합계가 Nums의 전체 합 - 왼쪽합계 - pivot 즉 오른쪽
            # 원소들의 합과 다르면 왼쪽의 합을 val 만큼 더한다.
            if sumLeft != sumNums - sumLeft - val:
                sumLeft += val
            else:
                # 같으면 i가 pivot 이 된다.
                return i

        # 무사히 반복문을 빠져나가면 pivot이 없으므로
        # -1 을 return 한다.
        return -1


if __name__ == "__main__":
    nums = [1, 7, 3, 6, 5, 6]
    #nums = [-1, -1, -1, 0, 1, 1]
    sl = Solution().pivotIndex(nums)
    print(sl)
