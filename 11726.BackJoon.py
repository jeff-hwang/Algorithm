# 2 x n 타일링
# DP

# 2xn 크기의 직사각형을 1x2, 2x1 타일로 채우는 방법의 수를 구하는 프로그램을 작성하시오.

# n 입력
import sys

sys.setrecursionlimit(10000)
n = int(input())

arr = [0 for i in range(1001)]


def dp(i):
    if i == 1:
        arr[1] = 1

    if i == 2 :
        arr[2] = 2

    if arr[i] != 0 :
        return arr[i]

    arr[i] = dp(i-1) + dp(i-2)
    
    return arr[i]

if n==1000:
    print((dp(n-1)+dp(n-2))%10007)

else:
    print(dp(n)%10007)
