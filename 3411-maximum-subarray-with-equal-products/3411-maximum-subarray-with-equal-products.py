import math
from typing import List

class Solution:
    def maxLength(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        max_limit = math.lcm(*nums) * max(nums)
        
        for i in range(n):
            prod = 1
            g = 0
            l = 1
            for j in range(i, n):
                prod *= nums[j]
                if prod > max_limit:
                    break
                
                g = math.gcd(g, nums[j])
                l = math.lcm(l, nums[j])
                
                if prod == l * g:
                    ans = max(ans, j - i + 1)
                    
        return ans
