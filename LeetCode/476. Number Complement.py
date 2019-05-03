class Solution(object):
    def findComplement(self, num):

        # 2진수를 2^0 ~ 2^n 까지 저장할 배열 변수
        bi = []

        # num 이 0 이 될때까지 반복을 돌림
        while num!=0:
            # 2로 나눈 나머지를 bi에 append
            bi.append(num%2)
            # 계산하였으므로 num 을 2로 나눔
            num = num//2
        
        # return 할 값
        answer = 0

        # bi를 0 제곱부터 N제곱까지 배치하였으므로
        # enumerate 함수를 사용하여 index를 그대로 사용하면 된다.
        for i, v in enumerate(bi):
            # v 값이 0이면 2^i 를 answer에 더한다
            if v == 0:
                answer += 2**i
        
        # return answer
        return answer

if __name__ == "__main__":
    sl = Solution().findComplement(5)
    print(sl)
