from typing import List

class Solution:
    def minSumSquareDiff(self, nums1: List[int], nums2: List[int], k1: int, k2: int) -> int:
        # Frequency array to count each absolute difference (max difference is 10^5)
        freq = [0] * (10**5 + 1)
        
        for a, b in zip(nums1, nums2):
            freq[abs(a - b)] += 1
            
        k = k1 + k2
        
        # Greedily reduce the largest differences down to smaller ones
        for i in range(100000, 0, -1):
            if freq[i] > 0:
                # How many operations we need to pull current `freq[i]` down to `i - 1`
                change = min(k, freq[i])
                freq[i] -= change
                freq[i - 1] += change
                k -= change
                
                if k == 0:
                    break
                    
        # Calculate the final sum of squared differences
        res = 0
        for i in range(100001):
            if freq[i] > 0:
                res += freq[i] * (i * i)
                
        return res
