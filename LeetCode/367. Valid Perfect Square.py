class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        # 정사각형인지 아닌지 확인

        # num 은 사각형의 넓이
        # 밑변 ^ 2 = 넓이
        # 넓이 ^ 0.5 = 밑변
        res = num**0.5

        # 계산하면 float 형이 나온다.
        # int로 형 변환 하였을 때 값의 크기가 변하지 않으면
        # True
        # 그렇지 않으면 False
        if res == int(res):
            return True
        else :
            return False