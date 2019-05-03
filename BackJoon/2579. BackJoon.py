stScore = []
# 계단의 수
stairs = int(input())

# 최대 300개의 계단이 존재
mxScore = [None] * 300

# 첫 번째 input 값에 따른 계단 별 점수를 받기위한
# input 반복
for i in range(stairs):
    stScore.append(int(input()))


# 점화식 dp[n] = max(dp[n-3] + arr[n-1] + arr[n], dp[n-2]+arr[n])
# 0~stair-1 까지 반복하여 그 계단까지 갈 수 있는 최대 점수를 계산
for i in range(stairs):
    # i 가 0 일땐 stScore[i] 가 최대값이 됨
    if i == 0:
        mxScore[0] = stScore[i]
        continue
    # i가 1 인 경우 0~1 까지 의 계단 점수를 더한 값이 최대값
    elif i == 1:
        mxScore[1] = stScore[0]+stScore[1]
        continue
    # i 값이 2 인 경우 0번과 1번 중 더 큰 계단 점수를 더해줌
    elif i == 2:
        mxScore[2] = max(stScore[0], stScore[1]) + stScore[2]
        continue

    # i가 3 이상인 경우 점화식에 따라 계산
    mxScore[i] = max(mxScore[i-3] + stScore[i-1], mxScore[i-2]) + stScore[i]

print(mxScore[stairs-1])
