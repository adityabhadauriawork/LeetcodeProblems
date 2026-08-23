class Solution:
    def sumGame(self, num: str) -> bool:
        left_sum = 0
        right_sum = 0
        left_marks = 0
        right_marks = 0
        n = len(num)
        half = n // 2
        
        for i in range(half):
            if num[i] == '?':
                left_marks += 1
            else:
                left_sum += int(num[i])
                
        for i in range(half, n):
            if num[i] == '?':
                right_marks += 1
            else:
                right_sum += int(num[i])
                
        # Total change expected from pairs of '?' is 9 per pair
        # Check if difference in sums accounts for the difference in question mark pairs * 9
        return (left_sum - right_sum) != (right_marks - left_marks) * 4.5
