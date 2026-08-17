class Solution:
    def stoneGameV(self, stoneValue: list[int]) -> int:
        n = len(stoneValue)
        
        # prefix[i] stores the sum of stones from index 0 to i-1
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + stoneValue[i]
            
        def get_sum(l, r):
            return prefix[r + 1] - prefix[l]

        # dp[i][j] = max score Alice can get from subarray i to j
        dp = [[0] * n for _ in range(n)]
        
        # max_l[i][j] = max( get_sum(i, k) + dp[i][k] ) for k in range(i, j+1)
        max_l = [[0] * n for _ in range(n)]
        
        # max_r[i][j] = max( get_sum(k, j) + dp[k][j] ) for k in range(i, j+1)
        max_r = [[0] * n for _ in range(n)]

        # Base cases initialization
        for i in range(n):
            max_l[i][i] = stoneValue[i]
            max_r[i][i] = stoneValue[i]

        # Fill DP table. i goes from right to left, j goes from left to right
        for i in range(n - 2, -1, -1):
            m = i  # Pivot pointer
            
            for j in range(i + 1, n):
                # Move pivot m to the point where left_sum >= right_sum
                while m < j - 1 and get_sum(i, m) < get_sum(m + 1, j):
                    m += 1
                
                res = 0
                
                # 1. Splits where left_sum < right_sum (k in range [i, m-1])
                # Alice is forced to take the left part.
                if m > i:
                    res = max(res, max_l[i][m - 1])
                    
                # 2. Splits where left_sum > right_sum (k in range [m+1, j-1])
                # Alice is forced to take the right part.
                if m < j - 1:
                    res = max(res, max_r[m + 1][j])
                    
                # 3. Check the exact pivot point m
                if get_sum(i, m) == get_sum(m + 1, j):
                    # Alice gets to choose the best among both sides
                    res = max(res, get_sum(i, m) + dp[i][m])
                    res = max(res, get_sum(m + 1, j) + dp[m + 1][j])
                elif get_sum(i, m) > get_sum(m + 1, j):
                    # left_sum > right_sum at m, Alice is forced to take the right part
                    res = max(res, get_sum(m + 1, j) + dp[m + 1][j])
                else:
                    # left_sum < right_sum at m (only happens if m reaches j-1 and left is still smaller)
                    res = max(res, get_sum(i, m) + dp[i][m])

                # Record the answer for this interval
                dp[i][j] = res
                
                # Update the running maximums for larger intervals to use in $O(1)$ time
                max_l[i][j] = max(max_l[i][j - 1], get_sum(i, j) + dp[i][j])
                max_r[i][j] = max(max_r[i + 1][j], get_sum(i, j) + dp[i][j])

        return dp[0][n - 1]