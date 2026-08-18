from collections import Counter

class Solution:
    def largestInteger(self, nums: list[int], k: int) -> int:
        n = len(nums)
        
        # Case 1: The entire array is the only subarray
        if k == n:
            return max(nums)
        
        # Count overall frequencies of each number
        counts = Counter(nums)
        
        # Case 2: Subarrays are of size 1
        if k == 1:
            # Find the maximum element that appears exactly once
            unique_elements = [num for num, count in counts.items() if count == 1]
            return max(unique_elements) if unique_elements else -1
            
        # Case 3: 1 < k < n
        # Only the first or last element can appear in exactly one subarray
        ans = -1
        if counts[nums[0]] == 1:
            ans = max(ans, nums[0])
        if counts[nums[-1]] == 1:
            ans = max(ans, nums[-1])
            
        return ans
