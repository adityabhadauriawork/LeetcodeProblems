class Solution:
    def numEquivDominoPairs(self, dominoes: list[list[int]]) -> int:
        from collections import Counter
        counts = Counter()
        pairs = 0
        for a, b in dominoes:
            key = (a, b) if a < b else (b, a)
            pairs += counts[key]
            counts[key] += 1
        return pairs
