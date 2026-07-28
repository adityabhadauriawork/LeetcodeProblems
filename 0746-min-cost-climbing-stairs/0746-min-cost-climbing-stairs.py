class Solution:
    def minCostClimbingStairs(self, cost):
        if len(cost) == 1:
            return cost[0]
        if cost == []:
            return 0
        # dp = [0]*len(cost)
        # dp[0]=cost[0]
        # dp[1]=cost[1]
        # for i in range(2, len(cost)):
        #     dp[i] = cost[i] + min(dp[i-1], dp[i-2])
        # return min(dp[-1],dp[-2])
        prev = cost[0]
        curr = cost[1]
        for i in range(2,len(cost)):
            new = cost[i]+min(prev, curr)
            prev = curr
            curr = new
        return min(prev,curr)