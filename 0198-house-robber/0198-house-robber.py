class Solution:
    # def rec(self,i,nums,dp):
    #     if i>=len(nums):
    #         return 0
    #     if dp[i]!=-1:
    #         return dp[i]
    #     #take case
    #     take = nums[i] + self.rec(i+2,nums,dp)

    #     #not take case
    #     not_take = self.rec(i+1,nums,dp)
    #     #before returning final return
    #     dp[i] = max(take,not_take)
    #     return dp[i]

    # def rob(self,nums):
    #     dp = [-1]*len(nums)
    #     return self.rec(0,nums,dp)
    def rob(self,nums):
        if len(nums) == 1:
            return nums[0]
        n = len(nums)
        dp = [0]*n
        dp[0] = nums[0]
        dp[1] = max(nums[0],nums[1])

        for i in range(2, n):
            not_take = dp[i - 1]
            take = nums[i] + dp[i-2]
            dp[i] = max(take, not_take)
        return dp[n-1]
        