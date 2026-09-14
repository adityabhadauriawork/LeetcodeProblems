class Solution:
    def isRectangleOverlap(self, rec1: list[int], rec2: list[int]) -> bool:
        # Check if X-axis intervals overlap and Y-axis intervals overlap
        return (rec1[0] < rec2[2] and rec2[0] < rec1[2] and  # X-axis overlap
                rec1[1] < rec2[3] and rec2[1] < rec1[3])    # Y-axis overlap
