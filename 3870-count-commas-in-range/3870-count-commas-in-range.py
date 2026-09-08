class Solution:
    def countCommas(self, n: int) -> int:
        total_commas = 0
        factor = 1000
        
        while factor <= n:
            total_commas += (n - factor + 1)
            factor *= 1000
            
        return total_commas
