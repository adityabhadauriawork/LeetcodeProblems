class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        closed_islands_count = 0

        def is_closed(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return False

            if grid[r][c] == 1:
                return True

            grid[r][c] = 1

            top = is_closed(r - 1, c)
            bottom = is_closed(r + 1, c)
            left = is_closed(r, c - 1)
            right = is_closed(r, c + 1)

            return top and bottom and left and right

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    if is_closed(r, c):
                        closed_islands_count += 1

        return closed_islands_count
