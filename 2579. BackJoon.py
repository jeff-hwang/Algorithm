stScore = []
stairs = int(input())
mxScore = [None] * 300
for i in range(stairs):
    stScore.append(int(input()))

for i in range(stairs):
    if i == 0:
        mxScore[0] = stScore[i]
        continue
    elif i == 1:
        mxScore[1] = stScore[0]+stScore[1]
        continue
    elif i == 2:
        mxScore[2] = max(stScore[0], stScore[1]) + stScore[2]
        continue

    mxScore[i] = max(mxScore[i-3] + stScore[i-1], mxScore[i-2]) + stScore[i]

print(mxScore[stairs-1])
