data = list(map(int, input().split(' ')))
N, M = data[0], data[1]

arr = [list(map(int, input().split(' '))) for i in range(N)]
#print(arr)
K = int(input())

arrPoint =[list(map(int, input().split(' '))) for i in range(K)]
#print(arrPoint)

dp = [[0 for j in range(301)] for i in range(301)]

dp[0][0] = arr[0][0]

for i in range(1, N):
    dp[i][0] = dp[i-1][0] + arr[i][0]


for i in range(1, M):
    dp[0][i] = dp[0][i-1] + arr[0][i]

for i in range(1, N):
    for j in range(1, M):
        dp[i][j] = dp[i][j-1]+dp[i-1][j] - dp[i-1][j-1]+ arr[i][j]


for av in arrPoint:
    i, j, x, y = av[0], av[1], av[2], av[3]
    print(dp[x-1][y-1]-dp[x-1][j-2]-dp[i-2][y-1]+dp[i-2][j-2])

