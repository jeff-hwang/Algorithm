def solution(triangle):
    triSize = len(triangle) # 삼각형 배열의 사이즈
    dp = [[0 for j in range(i+1)] for i in range(triSize)] # 각 경로의 최대 값을 저장해놓을 배열
    dp[0][0] = triangle[0][0] # 높이가 1 일 때는 경우의 수가 1개뿐
    if triSize == 1: # 높이가ㅏ 1 일 때는 계산을 마쳤으므로 바로 return
        return dp[0][0]
    for i in range(1, triSize): # 1부터 삼각형 배열의 사이즈 만큼 반복
        dp[i][0] = dp[i-1][0] + triangle[i][0] # 맨 앞의 경로는 한 가지 경우의 수 밖에 존재하지 않음
        dp[i][i] = dp[i-1][i-1] + triangle[i][i] # 맨 뒤도 마찮가지로 한가지 경우의 수 만 존재
        for j in range(1, i):
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j] # 각 경로의 최대 값은 자기 자신의 값과 이전 층의 2가지 경우 중 max 값임
    return max(dp[-1]) # dp 배열의 맨 마지막 값 중 max 값을 return

triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
sl = solution(triangle)
print(sl)
