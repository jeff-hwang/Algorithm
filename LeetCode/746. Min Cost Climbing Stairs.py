class Solution(object):
    def minCostClimbingStairs(self, cost):
        size = len(cost) # cost size
        dp = [cost[0] if i==0 else cost[1] if i==1 else 0 for i in range(size)] # 컴프리헨션을 하면서 i가 0, 1 일 때 초기화
        for i in range(2, size): dp[i] = cost[i] + min(dp[i-1], dp[i-2]) # dp[i] = cost[i] + min(dp[i-1]+dp[i-2])
        return min(dp[size-2], dp[size-3]+cost[i]) # 지역변수 i 가 살아있음 신기..

sl = Solution().minCostClimbingStairs([1, 100, 1,1,1,100,1,1,100,1])
print(sl)
        