class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)
        sm , lg = min(s), max(s)
        if list(s) == sorted(s):
            return 0
        if n == 2:
            return -1
        if s[0] == sm or s[-1] == lg:
            return 1
        if lg in s[1:-1] or sm in s[1:-1]:
            return 2
        return 3
        