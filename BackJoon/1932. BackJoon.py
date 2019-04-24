# 층의 수
N = int(input())

# 경로마다 가질 수 있는 최대의 값을 저장하는 변수
arr = []

for i in range(N):
    # 층 별로 빈 칸을 기준으로 integer 배열을 생성
    line = list(map(int, input().split(" ")))
    arr.append(line)

# 점화식
# dp[i] = max(dp[i][j-1], dp[i][j]) + arr[i][j]

# 첫 번째 줄인 경우는 값 변경이 필요 없음
# 1부터 N 까지 반복
for i in range(1, N):
    # i 번째 층의 길이
    ln = len(arr[i])

    # 0 ~ ln 까지 반복하면 층의 원소들을 계산
    for j in range(ln):    
        # 층의 맨 앞자리 값은 이전 층의 첫 번째 값을 더한 것
        if j == 0:
            arr[i][j] += arr[i-1][j]
            continue
        
        # 층의 마지막 자리 값은 이전 층의 마지막 값을 더한 것
        if j == ln-1:
            arr[i][j] += arr[i-1][j-1]
            continue
        
        # 그 외는 점화식에 따라 계산
        arr[i][j] += max(arr[i-1][j-1], arr[i-1][j])

# 마지막 층의 최대 값을 출력
print(max(arr[N-1]))