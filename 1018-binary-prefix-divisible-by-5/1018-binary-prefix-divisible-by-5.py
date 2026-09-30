class Solution:
    def prefixesDivBy5(self, nums: list[int]) -> list[bool]:
        res = []
        val = 0
        for num in nums:
            val = (val * 2 + num) % 5
            res.append(val == 0)
        return res
