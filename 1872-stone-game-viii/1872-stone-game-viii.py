from itertools import accumulate
from typing import List

class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        s = list(accumulate(stones))
        res = s[-1]
        for i in range(len(stones) - 2, 0, -1):
            res = max(res, s[i] - res)
        return res
