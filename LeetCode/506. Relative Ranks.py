class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """

        # 초기 nums의 인덱스를 저장할 딕셔너리
        dic = {}
        
        # nums의 크기
        size = len(nums)

        # nums의 크기만큼 비어있는 list 생성 - 결과를 저장
        res = [None]*size
        
        # size 만큼 반복을 하여 dic변수에 저장
        for i in range(size):
            dic[nums[i]] = i
          
        # nums를 오름차순으로 정렬
        # nums를 내림차순으로 정렬하지 않는 이유는
        # 시간복잡도가 2배만큼 더 걸리기 때문
        nums.sort()
        
        # size-1 ~ 0 까지 반복
        for i in range(size-1,-1,-1):
            # 1 등이면 금메달
            if size-1-i == 0:
                res[dic[nums[i]]] = "Gold Medal"

            # 2등이면 은메달
            elif size-1-i == 1:
                res[dic[nums[i]]] = "Silver Medal"
            
            # 3등이면 동메달
            elif size-1-i == 2:
                res[dic[nums[i]]] = "Bronze Medal"

            # 나머지면 순위 그대로
            else:
                res[dic[nums[i]]] = str(size-i)
        
        # 결과값 리턴
        return res    
