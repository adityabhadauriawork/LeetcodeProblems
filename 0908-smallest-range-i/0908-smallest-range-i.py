class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        d = max(nums) - min(nums)
        return max(0, d - 2 * k)