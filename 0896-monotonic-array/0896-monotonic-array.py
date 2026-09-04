class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        inc = dec = True
        for a, b in zip(nums, nums[1:]):
            if a > b:
                inc = False
            if a < b:
                dec = False
        return inc or dec