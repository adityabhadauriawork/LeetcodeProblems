class Solution:
    def minimumDeletions(self, nums: list[int]) -> int:
        n = len(nums)
        min_idx = nums.index(min(nums))
        max_idx = nums.index(max(nums))
        
        # Ensure min_idx is the smaller index and max_idx is the larger
        i, j = sorted([min_idx, max_idx])
        
        # Three possible deletion strategies:
        # 1. Delete all elements from the front (up to the rightmost index `j`)
        front_only = j + 1
        
        # 2. Delete all elements from the back (from the leftmost index `i` to the end)
        back_only = n - i
        
        # 3. Delete from both ends (front up to `i`, and back starting from `j`)
        both_ends = (i + 1) + (n - j)
        
        return min(front_only, back_only, both_ends)
