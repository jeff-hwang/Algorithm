# input 처리
N = int(input())
arr = list(map(int, input().split(" ")))

# 최대 10만 까지의 배열을 생성
dp = [None for i in range(100000)]

# arr의 합을 저장할 변수
sumData = 0

# dp[0] 은 무조건 arr[0]
dp[0] = arr[0]

# sumData 에 i 번째 배열까지 최대로 나올 수 있는 연속합을 저장
sumData += dp[0]

# input Data 가 1 이상일 때
# dp[i] = max(sumData, dp[i-1])
if N > 1 :
    for i in range(1, N):
        # 연속 합이 음수 일 경우 sumData를 0으로 초기화 해준다.
        if sumData <= 0:
            sumData = 0

        sumData += arr[i]
        
        dp[i] = max(sumData, dp[i-1])
        
    print(dp[N-1])

# input Data 가 1 일때 처리
else :
    print(dp[N-1])
            
        
