# 집 수
N = int(input())

houses = []
# 각 집의 RGB 색 비용
for i in range(N):
    houses.append([int(data) for data in input().split(" ")])

# dp = [0,0,0] * N 으로 dp 배열을 생성하면 call by reference 발생해서 오류난다.
dp =  [[0 for i in range(3)] for j in range(N)]

def dynamic(N, dp, houses):
    for i in range(N):
        if i == 0:
            dp[i][0] = houses[0][0]
            dp[i][1] = houses[0][1]
            dp[i][2] = houses[0][2]

        else :
            dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + houses[i][0]
            dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + houses[i][1]
            dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + houses[i][2]

    print(min(dp[N-1]))

dynamic(N, dp, houses)


        

