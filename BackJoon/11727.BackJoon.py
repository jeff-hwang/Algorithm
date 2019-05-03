N = int(input())
dp = [0 for i in range(1000)]
dp[0] = 1
dp[1] = 3
dp[2] = 5

for i in range(3, N):
    dp[i] = dp[i-1] + (2*dp[i-2])

print(dp[N-1]%10007)
