class Solution:
    def maxAlternatingSum(self, nums: list[int]) -> int:
        # Square each element
        squares = [x * x for x in nums]
        
        # Sort squares in ascending order
        squares.sort()
        
        n = len(squares)
        mid = n // 2
        
        # The smaller half is subtracted, the larger half is added
        return sum(squares[mid:]) - sum(squares[:mid])
