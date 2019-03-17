class Solution:
    def largestPerimeter(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        # 내림차순으로 정렬
        A.sort(reverse=True)
        # enumerate 는 index 값과 value 값을 가져올 수 있음
        for i, elem in enumerate(A[:-2]):
            temp = A[i+1] + A[i+2]
            if elem < temp:
                return elem + temp
            
        return 0

sl = Solution()
print(sl.largestPerimeter([1,2,1]))