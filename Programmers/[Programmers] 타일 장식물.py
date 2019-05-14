def solution(N):
    
    dp = [0 for i in range(80)]
    dp[0] = 1
    dp[1] = 2

    if N == 1 :
        return 4
    elif N == 2:
        return 6 
    for i in range(2, N):
        dp[i] = dp[i-1]+dp[i-2]
    

    return 2*(dp[N-1]+dp[N-2])

print(solution(3))