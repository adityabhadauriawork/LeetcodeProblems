class Solution:

    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        freq = {}
        for i in range(len(prices)):
            for j in range(i+1,len(prices)):
                if prices[j] > prices[i]:
                    ans = prices[j] - prices[i]
                    if ans not in freq:
                        freq[ans] = 1
                    else:
                        freq[ans]+=1
        if len(freq) == 0:
            return 0
        else:
            return max(freq.keys())
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        dp = {}
        dp[0] = 0
        min_price = prices[0]
        for i in range(1, len(prices)):
            min_price = min(min_price, prices[i])
            profit_today = prices[i] - min_price
            dp[i] = max(dp[i - 1], profit_today)

        return dp[len(prices) - 1]