from typing import List

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)

        total = sum(cardPoints)

        if k == n:
            return total

        window = n - k

        curr = sum(cardPoints[:window])
        minimum = curr

        for i in range(window, n):
            curr += cardPoints[i]
            curr -= cardPoints[i - window]
            minimum = min(minimum, curr)

        return total - minimum