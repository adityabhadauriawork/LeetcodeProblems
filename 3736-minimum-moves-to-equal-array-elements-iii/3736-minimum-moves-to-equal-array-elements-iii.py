class Solution:
    def minMoves(self, nums: List[int]) -> int:
        count = 0
        a = max(nums)
        for b in nums:
            if b != a:
                count+= a-b
            if b == a:
                continue
        return count
        
        