class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        res = []
        i = 0
        while i < len(nums):
            start = nums[i]
            while i + 1 < len(nums) and nums[i+1] == nums[i] + 1:
                i += 1
            if start != nums[i]:
                res.append(f"{start}->{nums[i]}")
            else:
                res.append(f"{start}")
            i += 1
        return res
