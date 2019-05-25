N, K = list(map(int,input().split()))
coin = [int(input()) for i in range(N)]
coin.sort()  # 동전 내림차순 정렬
dp = [0 for i in range(K+1)]
if coin[0] > K:
    print(0)
else :
    dp[0] = 1
    for i in range(N):
        for j in range(coin[i], K+1):
            dp[j] += dp[j-coin[i]]

print(dp[K])
            