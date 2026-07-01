from typing import List

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        counter = 0
        freq_row = {}

        # Count the frequency of each row
        for row in grid:
            row = tuple(row)
            freq_row[row] = freq_row.get(row, 0) + 1

        # Check each column
        for col in range(len(grid)):
            column = []

            for r in range(len(grid)):
                column.append(grid[r][col])

            column = tuple(column)

            if column in freq_row:
                counter += freq_row[column]

        return counter