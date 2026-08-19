import collections
from typing import List

class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        row_to_seats = collections.defaultdict(int)
        
        # Mark reserved seats using bit flags (0 to 9 for columns 1 to 10)
        for row, seat in reservedSeats:
            row_to_seats[row] |= 1 << (seat - 1)
            
        ans = 0
        for seats in row_to_seats.values():
            # Check left, middle, and right 4-person blocks
            can_left = (seats & 0b0111100000) == 0  # seats 2,3,4,5
            can_right = (seats & 0b0000011110) == 0 # seats 6,7,8,9
            can_mid = (seats & 0b0001111000) == 0   # seats 4,5,6,7
            
            if can_left and can_right:
                ans += 2
            elif can_left or can_right or can_mid:
                ans += 1
                
        # Rows with no reservations can fit 2 groups each
        ans += (n - len(row_to_seats)) * 2
        return ans

