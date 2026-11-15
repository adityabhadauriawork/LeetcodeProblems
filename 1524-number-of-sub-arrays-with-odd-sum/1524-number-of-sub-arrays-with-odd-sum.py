class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        MOD = 10**9 + 7
        count = 0
        prefix_sum = 0
        
        # Start with even_count = 1 to account for an empty prefix (sum = 0)
        even_count = 1
        odd_count = 0
        
        for num in arr:
            prefix_sum += num
            
            if prefix_sum % 2 == 0:
                count += odd_count
                even_count += 1
            else:
                count += even_count
                odd_count += 1
                
        return count % MOD
