'''
포도주 잔을 선택하면 그 잔에 들어있는 포도주는 모두 마셔야 하고, 마신 후에는 원래 위치에 다시 놓아야 한다.
연속으로 놓여 있는 3잔을 모두 마실 수는 없다.
'''

N = int(input())
arr = [int(input()) for i in range(N)]

dp = [0 for i in range(10000)]

try:
    dp[0] = arr[0]
    dp[1] = arr[0]+arr[1]
    dp[2] = max(arr[0]+arr[2], arr[1]+arr[2], dp[1])
    
except:
    pass

if N < 3:
    print(dp[N-1])
else :
    for i in range(3, N):
        dp[i] = max(dp[i-3] + arr[i-1] + arr[i], dp[i-2] + arr[i], dp[i-1])

    print(dp[N-1])




