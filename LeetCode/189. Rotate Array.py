class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # 문제 설명
        '''
        nums 배열이 input으로 주어지는데
        뒤에서 부터 k 개를 꺼내 앞으로 붙여라

        ex) nums = [1,2,3,4,5,6,7]
            k = 3

            step 1 :  [7,1,2,3,4,5,6]
            step 2 :  [6,7,1,2,3,4,5]
            step 3 :  [5,6,7,1,2,3,4]

        '''
        # nums 의 길이를 구다
        ln = len(nums)
        
        # k 번 반복하여 nums의 맨 마지막 원소를 꺼내
        # 0번 인덱스에 삽입한다.
        for i in range(k):
            nums.insert(0, nums.pop(ln-1))      
        

if __name__ == "__main__":
    nums = [1,2,3,4,5,6,7]
    k = 3
    print(Solution().rotate(nums, k))