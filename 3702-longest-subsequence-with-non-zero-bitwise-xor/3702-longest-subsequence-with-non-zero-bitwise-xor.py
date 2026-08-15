class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        n = len(nums)
        xor_sum = 0
        zero_count = 0
        
        for x in nums:
            xor_sum ^= x
            if x == 0:
                zero_count += 1
                
        # Case 1: Total XOR is already non-zero, take all elements
        if xor_sum != 0:
            return n
            
        # Case 2: All elements are zeros, no non-zero XOR possible
        if zero_count == n:
            return 0
            
        # Case 3: Total XOR is 0, but there are non-zero elements; drop one element
        return n - 1



