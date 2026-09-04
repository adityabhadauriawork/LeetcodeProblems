class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        n = len(grid)
        xy = sum(x > 0 for row in grid for x in row)
        xz = sum(map(max, grid))
        yz = sum(max(grid[i][j] for i in range(n)) for j in range(n))
        return xy + xz + yz