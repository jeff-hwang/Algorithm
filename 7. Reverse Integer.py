class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        # 문제 설명
        '''
            input 으로 [-2^31, 2^31-1] 범위의 정수를 받는데
            이 수를 거꾸로 뒤집어 표현하라.
            단, 음수는  '-' 가 먼저 보이도록 하고,
            input 범위를 초과할 시 0 을 return 하라.
            0이 맨 앞에 나올 경우 skip.. 하고 다음 숫자부터 표현. 
        '''

        rst = "" # 결과를 return할 변수
        xStr = str(x) # input Data를 String 으로 여러번 변환하지 않기 위해 변수 선언
        ln = len(xStr) # x의 길이

        # ln-1 부터 0 번까지의 index를 1만큼 감소시키기 위한 for 문
        for i in range(ln-1, -1, -1):
            # 만약 맨 뒤의 숫자가 0 인경우 continue
            if i==ln-1 and str(x)[i]==0:
                continue
            # 맨 마지막 글자가 - 인경우 맨 앞으로 붙여 rst에 붙임
            # 그 다음 break를 하여 반복문을 빠져나감
            if i==0 and str(x)[0]=="-":
                rst = xStr[0]+rst
                break
            # 뒤에서 부터 차례로 rst에 붙임
            rst += xStr[i] 

        # 문자열을 다시 Integer 형태로 변환
        rst = int(rst)
        
        # 조건 범위에 부적합하면 0, 적합하다면 rst를 return 한다.
        if rst <= 2**31-1 and rst >= -2**31:
            return rst
        else:
            return 0
        

if __name__ == "__main__":
    x = 123
    sl = Solution().reverse(x)
    print(sl)