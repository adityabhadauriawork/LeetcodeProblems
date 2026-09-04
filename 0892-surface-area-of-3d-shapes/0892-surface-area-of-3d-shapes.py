class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        n = len(grid)
        area = 0
        for i in range(n):
            for j in range(n):
                h = grid[i][j]
                if h:
                    area += 2 + 4 * h
                    if i > 0:
                        area -= 2 * min(h, grid[i - 1][j])
                    if j > 0:
                        area -= 2 * min(h, grid[i][j - 1])
        return area