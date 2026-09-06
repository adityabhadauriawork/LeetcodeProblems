class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        
        # If the target string is longer than the source string, 
        # it's impossible to form t from s.
        if n > m:
            return 0
            
        # dp[j] stores the number of distinct subsequences matching t[0...j-1]
        dp = [1] + [0] * n
        
        for i in range(1, m + 1):
            # Iterate backwards to use the values from the previous row 
            # without overwriting them prematurely
            for j in range(n, 0, -1):
                if s[i - 1] == t[j - 1]:
                    dp[j] += dp[j - 1]
                    
        return dp[n]
