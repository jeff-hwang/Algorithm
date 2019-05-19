def solution(n):
    dp = [0 for i in range(n)]
    dp[0] = 1
    dp[1] = 2
    dp[2] = 3
    if n < 4:
        return dp[n-1]
    for i in range(3, n):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n-1]%1000000007