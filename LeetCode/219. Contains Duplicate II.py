class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        # nums가 중복이 없다면 return False
        if len(set(nums)) == len(nums):
            return False
        
        # nums 의 크기
        size = len(nums)
        
        
        # nums 를 index와 value 를 하나하나 꺼내서 비교해본다.
        for i, v in enumerate(nums):
            # 여기서 out of range exception이 발생할 수 있기에
            # try except 를 해준다.
            try:
                # 문제에서 index간의 거리가 최대 k 인 value를 비교하라 하였으므로
                # value가 같다면 return True를 해주고 method를 종료한다.
                for j in range(1, k+1):
                    if v == nums[i+j]:
                        return True
            except:
                # out of range Exception 이 발생하면 반복문을 건너뛴다.
                pass
            
        # 위의 코드에서 무사히 여기까지 온다면 문제에서 True의 조건에 해당하지 않으므로
        # return False를 한다.
        return False