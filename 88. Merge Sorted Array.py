class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        # nums1의 m번 인덱스부터 끝까지 삭제
        del nums1[m:]
        
        # nums1 에 nums2의 0~n-1 인덱스 원소들 추가
        nums1 += nums2[0:n]
        # 오름차순으로 정렬
        nums1.sort()
        return nums1

nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
print(Solution().merge(nums1,m,nums2, n))