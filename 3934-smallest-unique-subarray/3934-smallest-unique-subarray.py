from collections import Counter
from typing import List


class Solution:
    def smallestUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        base1, mod1 = 1315423911, 10**9 + 7
        base2, mod2 = 131313131, 10**9 + 9

        def has_unique(length: int) -> bool:
            h1 = 0
            h2 = 0
            p1 = pow(base1, length - 1, mod1)
            p2 = pow(base2, length - 1, mod2)

            for i in range(length):
                h1 = (h1 * base1 + nums[i]) % mod1
                h2 = (h2 * base2 + nums[i]) % mod2

            counts = Counter([(h1, h2)])

            for i in range(length, n):
                h1 = ((h1 - nums[i - length] * p1) * base1 + nums[i]) % mod1
                h2 = ((h2 - nums[i - length] * p2) * base2 + nums[i]) % mod2
                counts[(h1, h2)] += 1

            return 1 in counts.values()

        low, high = 1, n
        ans = n

        while low <= high:
            mid = (low + high) // 2
            if has_unique(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans
