import math
from typing import List

class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        n = len(coins)
        
       
        subsets = []
        for mask in range(1, 1 << n):
            sub_lcm = 1
            count = 0
            for i in range(n):
                if (mask >> i) & 1:
                    count += 1
                    sub_lcm = math.lcm(sub_lcm, coins[i]) 
            
            sign = 1 if count % 2 == 1 else -1
            subsets.append((sub_lcm, sign))
            
        def count_less_equal(target: int) -> int:
            total = 0
            for lcm_val, sign in subsets:
                total += sign * (target // lcm_val)
            return total

        low = min(coins)
        high = min(coins) * k
        ans = high
        
        while low <= high:
            mid = (low + high) // 2
            if count_less_equal(mid) >= k:
                ans = mid
                high = mid - 1  
            else:
                low = mid + 1   
                
        return ans
