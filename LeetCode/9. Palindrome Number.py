class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        
        # 음수이면 무조건 False
        if x < 0:
            return False
        # 수가 한 자리 수이면 True
        elif x>=0 and x<10:
            return True
        
        # 파라미터를 String 형변환
        data = str(x)
        # String을 List 형태로 형변환
        data = list(data)
        # List 길이 저장
        lenData = len(data)

        # 길이가 짝수인 데이터 처리
        if lenData % 2 == 0:
            # 데이터 길이를 반으로 나누어
            # 앞 뒤로 대칭되는 것을 확인
            for i in range(0, (lenData/2) +1) :
                if data[i] == data[lenData-1-i]:
                    pass
                # 만약 대칭 되지 않았다면 return False
                else :
                    return False
            
            # 무사 통과하면 return True
            return True
        
        #홀수
        else :
            # 홀수의 데이터 길이는 반으로 나눌 경우 실수형태이므로
            # 절대값을 붙여준다
            for i in range(0, abs(lenData/2)):
                if data[i] == data[lenData-1-i]:
                    pass
                # 대칭이 아니면 return False
                else :
                    return False
            
            # 대칭인 경우 return True
            return True