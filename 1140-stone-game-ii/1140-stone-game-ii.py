from functools import lru_cache
from itertools import accumulate

class Solution:
    def stoneGameII(self, piles: list[int]) -> int:
        n = len(piles)
        # Suffix sums to quickly get the sum of remaining piles from index i to end
        s = list(accumulate(piles[::-1]))[::-1]
        
        @lru_cache(None)
        def dp(i: int, m: int) -> int:
            if i + 2 * m >= n:
                return s[i]
            # Maximize current player's stones by subtracting opponent's optimal result from remaining suffix sum
            return max(s[i] - dp(i + x, max(m, x)) for x in range(1, 2 * m + 1))
            
        return dp(0, 1)
