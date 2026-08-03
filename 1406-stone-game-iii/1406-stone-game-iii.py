import math

class Solution:
    def stoneGameIII(self, stoneValue: list[int]) -> str:
        n = len(stoneValue)
        # dp[i] represents the maximum score difference (current player - opponent) 
        # starting from index i to the end of the array.
        dp = [-math.inf] * n + [0]
        
        for i in reversed(range(n)):
            summ = 0
            for j in range(i, min(i + 3, n)):
                summ += stoneValue[j]
                dp[i] = max(dp[i], summ - dp[j + 1])
                
        if dp[0] == 0:
            return "Tie"
        return "Alice" if dp[0] > 0 else "Bob"
