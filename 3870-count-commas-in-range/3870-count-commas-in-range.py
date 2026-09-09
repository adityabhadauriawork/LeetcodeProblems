class Solution:
    def countCommas(self, n: int) -> int:
        ans = 0

        for i in range(1, n + 1):
            formatted = f"{i:,}"
            ans += formatted.count(",")

        return ans