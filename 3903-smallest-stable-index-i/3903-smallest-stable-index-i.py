class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        
        # Step 1: Precompute suffix minimums
        right = [nums[-1]] * n
        for i in range(n - 2, -1, -1):
            right[i] = min(right[i + 1], nums[i])
        
        # Step 2: Traverse with prefix maximums
        left = float('-inf')
        for i, x in enumerate(nums):
            left = max(left, x)
            if left - right[i] <= k:
                return i
        
        return -1
