class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # 비어있는 딕셔너리 변수 선언
        dic = {}

        # 파라미터 nums 를 하나하나 돌려본다.
        for i in nums : 
            # 만약 dicCount 의 return 값이 True 이면 중복임
            if self.dicCount(dic, i) == True:
                # 더 이상 진행할 필요없으므로 return True
                return True
        # 반복문을 무사히 빠져나오면 중복된 적이 없으므로 False
        return False
            
    # [{num, count}]
    def dicCount(self, dic, key):
        # 이미 존재하는 키이면 value를 1 증가
        try :
            dic[key] += 1
            return True
        # 존재하지 않으면 처음 나온 것이므로 1을 대입
        except :
            dic[key] = 1
        return False

        
if __name__ == "__main__":

    inData = [1,2,3,1]
    sl = Solution().containsDuplicate(inData)