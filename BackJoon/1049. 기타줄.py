N, M = list(map(int, input().split()))

m1 = 100000
m2 = 100000
res = None
for i in range(M):
    res = list(map(int, input().split()))
    m1 = min(m1, res[0]) # 패키지 최소값
    m2 = min(m2, res[1]) # 낱개 최소값

if N > 6 :# 끊어진 줄의 갯수가 6 초과인 경우
    remain = N % 6 # 6으로 나눈 나머지
    quotient = N // 6 # 6으로 나눈 몫
    # 최소 금액 패키지를 하나 초과 구매 case -> m1*((quotient)+1)
    # 최소 금액 패키지를 딱 맞게 구매 + 최소 낱개 금액 * N case -> m1*quotient + m2 * remain
    # 최소 낱개 금액 * N -> m2 * N
    res = [m1*((quotient)+1), m1*quotient + m2 * remain, m2 * N]
    if remain*m2 > m1 : # 나머지와 최소 낱개 곱이 m1 보다 큰 경우
        res = min(res[0:2])
    else :
        res = min(res)
else :
    res = min(m1, m2*N)
print(res)
        
