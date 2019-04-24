import sys

# N 자리 이(친수) 구하기
N = int(sys.stdin.readline())

arr = [0 for i in range(92)]

# N이 한자리이면 1
arr[1] = 1
# 두자리이면 10
arr[2] = 1
# 세자리이면 100, 101
arr[3] = 2

# 점화식 dp[i] = dp[i-1] + dp[i-2]

if N <= 3:
    sys.stdout.write(str(arr[N]))
else :
    for i in range(3, N+1):
        arr[i] = arr[i-1] + arr[i-2]
    
    sys.stdout.write(str(arr[N]))
