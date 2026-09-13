from functools import lru_cache
from bisect import bisect_right
import math

class Solution:
    def maximumWeight(self, intervals: list[list[int]]) -> list[int]:

        intervals = sorted(
            (*interval, i)
            for i, interval in enumerate(intervals)
        )

        @lru_cache(None)
        def dp(i, k):
            if i == len(intervals) or k == 0:
                return (0, ())

            # Don't take current interval
            skip = dp(i + 1, k)

            l, r, weight, idx = intervals[i]

            # First interval whose start > current r
            j = bisect_right(intervals, (r, math.inf))

            nxt = dp(j, k - 1)

            # Take current interval
            take = (
                weight + nxt[0],
                tuple(sorted((idx,) + nxt[1]))
            )

            # Maximum weight
            if take[0] > skip[0]:
                return take

            if take[0] < skip[0]:
                return skip

            # Same weight → lexicographically smaller indices
            return min(take, skip, key=lambda x: x[1])

        return list(dp(0, 4)[1])