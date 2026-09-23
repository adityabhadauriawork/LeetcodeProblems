class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        total_sum = sum(nums)
        target = total_sum - x
        
        # If the sum of all elements equals x, we must remove the entire array
        if target == 0:
            return len(nums)
        
        # If the sum of all elements is less than x, it's impossible to reach 0
        if target < 0:
            return -1
            
        max_len = -1
        current_sum = 0
        left = 0
        
        # Sliding window to find the longest subarray that sums up to 'target'
        for right in range(len(nums)):
            current_sum += nums[right]
            
            # Shrink the window from the left if the current sum exceeds the target
            while current_sum > target and left <= right:
                current_sum -= nums[left]
                left += 1
                
            # If we find a valid window, update the maximum length
            if current_sum == target:
                max_len = max(max_len, right - left + 1)
                
        # If max_len was updated, the operations count is total length minus max_len
        return len(nums) - max_len if max_len != -1 else -1
