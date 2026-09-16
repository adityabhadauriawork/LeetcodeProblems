class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        MOD = 1_000_000_007
        # We need to choose 2 * k points out of n + k - 1 points
        return math.comb(n + k - 1, 2 * k) % MOD
