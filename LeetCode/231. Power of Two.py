class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        '''
        문제설명
        n 이 2의 거듭제곱이면 True,
        그렇지 않으면 False를 Return 하라.
        '''
        # 반복문이 몇 번 돌았는지 체크해주는
        # count 변수
        cnt = 0

        while True:
            # 만약 2 ** cnt 가 n 이면 거듭제곱
            # Return True
            if 2 ** cnt == n:
                return True
            # 만약 거듭제곱이 n 보다 크면
            # 반복할 필요 없으니 
            if 2 ** cnt > n : 
                return False
            
            # cnt 를 1 증가 시킴
            cnt += 1

        return False


if __name__ == "__main__":
    input = 1
    sl = Solution().isPowerOfTwo(input)
    print(sl)
    