from typing import List
import bisect

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()

        n = len(potions)
        ans = []

        for spell in spells:
            need = (success + spell - 1) // spell   # Ceiling division

            idx = bisect.bisect_left(potions, need)

            ans.append(n - idx)

        return ans