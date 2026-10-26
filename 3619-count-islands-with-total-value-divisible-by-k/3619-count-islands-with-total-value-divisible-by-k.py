class Solution:
    def countIslands(self, grid: list[list[int]], k: int) -> int:
        R, C = len(grid), len(grid[0])
        ans = 0
        for r in range(R):
            for c in range(C):
                if grid[r][c] > 0:
                    total = grid[r][c]
                    grid[r][c] = 0
                    stack = [(r, c)]
                    while stack:
                        curr_r, curr_c = stack.pop()
                        for dr, dc in ((curr_r+1, curr_c), (curr_r-1, curr_c), (curr_r, curr_c+1), (curr_r, curr_c-1)):
                            if 0 <= dr < R and 0 <= dc < C and grid[dr][dc] > 0:
                                total += grid[dr][dc]
                                grid[dr][dc] = 0
                                stack.append((dr, dc))
                    if total % k == 0:
                        ans += 1
        return ans
