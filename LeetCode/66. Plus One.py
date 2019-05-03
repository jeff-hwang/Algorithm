class Solution(object):
    def plusOne(self, digits):

        # 결과값 담을 변수
        rst = []

        # digits 의 길이
        ln = len(digits)
        # 원소가 10이 넘을 때 1증가 해줄 캐리 변수
        carry = 0

        # digits 의 맨 마지막 원소를 1을 증가시키고 반복문에 들어감
        digits[-1] += 1

        # 역순으로 ln-1 부터 0번 인덱스까지 반복
        for i in range(ln-1, -1, -1):
            # dig는 각 자릿수 + carry 변수
            dig = digits[i]+carry
            # dig가 10이상이면 carry가 발생
            if dig >= 10:
                # rst의 맨 앞의 인덱스에 dig-10 을 삽입
                rst.insert(0, dig - 10)
                # carry 발생
                carry = 1
            else:
                # rst 맨앞에 dig 삽입
                rst.insert(0, dig)
                # carry가 존재하지 않음
                carry = 0

        # 반복문을 빠져나온 후 캐리가 있므면 맨앞에 삽입
        if carry != 0:
            rst.insert(0, carry)

        # rst 를 리턴 시킴
        return rst
