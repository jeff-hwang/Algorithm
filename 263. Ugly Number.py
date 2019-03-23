class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        # num 이 0보다 같거나 작으면 False
        if num <= 0 :
            return False
        
        
        while True:
            # num 을 2로 나눈 나머지가 0 일 때 pass
            if num % 2 == 0:
                num /= 2 
                pass

            # num 을 3로 나눈 나머지가 0 일 때 pass
            elif num % 3 == 0:
                num /= 3
                pass

            # num 을 5로 나눈 나머지가 0 일 때 pass
            elif num % 5 == 0:
                num /= 5
                pass
            
            # num == 1 일 때 조건이 만족됨 Return True
            elif num == 1:
                return True

            # 위의 case들을 통과 못하였기에 ugly number가 아니다.
            else :
                return False
            