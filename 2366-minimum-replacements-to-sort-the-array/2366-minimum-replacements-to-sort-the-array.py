class Solution:
    def minimumReplacement(self, nums):
        ans = 0
        prev = nums[-1]

        for i in range(len(nums) - 2, -1, -1):
            if nums[i] <= prev:
                prev = nums[i]
            else:
                parts = (nums[i] + prev - 1) // prev
                ans += parts - 1
                prev = nums[i] // parts

        return ans