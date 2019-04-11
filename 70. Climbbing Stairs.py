'''
문제 설명
- 계단오르기 문제
계단을 오를 때 두 가지 방법이 있는데
첫 번째, 한 칸씩 오른다.
두 번째, 두 칸씩 오른다.

if stairs == 1:
    return 1
    # 계단을 한 칸 오르는 법은 한칸 오르는 한가지 방법 뿐
if stairs == 2 :
    # 계단이 두 칸 일 경우
    return 2

    첫 번째, 한 칸씩 두 번에
    두 번째, 두 칸을 한 번에
'''


class Solution(object):
    # 전역변수를 적당히 크게 만들어 계단오르는 것을
    # 중복해서 계산하지 않도록 List 에 저장하여 사용
    nList = [None] * 10000

    def climbStairs(self, n):
        '''
        1 : 1
        2 : 2
        3 : 3
        4 : 5
        5 : 11
        .
        .
        .
        .

        점화식을 계산해 보면
        stairs(N) = sum(x for i in staris(N))
        즉, 1~N-1 까지의 계단오르는 방법을 다 더하는 것이다.
        '''

        # 계단이 한 칸일 경우
        if n == 1:
            # 전역변수 nList[0] 에 한가지 경우의 수라고 저장
            self.nList[0] = 1
            # nList의 0 번째 element return
            return self.nList[0]
        # 계단이 두 칸일 경우
        elif n == 2:
            # nList[1] 에 2를 저장
            self.nList[1] = 2
            # 전역변수 nList의 1번 element를 return
            return self.nList[1]

        # 만약 nList[n]에 값이 존재할 때
        # n번째 element return 한다.
        if self.nList[n] != None:
            return self.nList[n]

        # n번째 element에 값이 존재하지 않을경우 n-1 , n-2 의 결과 값을 더하여
        # return 한다
        # 피보나치 수열과 동일
        self.nList[n] = self.climbStairs(n-1) + self. climbStairs(n-2)
        return self.nList[n]
