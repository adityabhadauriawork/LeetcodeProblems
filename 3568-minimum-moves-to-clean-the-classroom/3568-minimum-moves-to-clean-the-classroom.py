from collections import deque

class Solution:
    def minMoves(self, classroom: list[str], energy: int) -> int:
        m, n = len(classroom), len(classroom[0])

        litter = {}
        start = None

        for i in range(m):
            for j in range(n):
                if classroom[i][j] == 'L':
                    litter[(i, j)] = len(litter)
                elif classroom[i][j] == 'S':
                    start = (i, j)

        k = len(litter)

        if k == 0:
            return 0

        full_mask = (1 << k) - 1
        start_mask = 0

        if start in litter:
            start_mask |= 1 << litter[start]

        # state = (row, col, energy, mask)
        q = deque([(start[0], start[1], energy, start_mask)])
        visited = {(start[0], start[1], energy, start_mask)}

        moves = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while q:
            for _ in range(len(q)):
                r, c, e, mask = q.popleft()

                if mask == full_mask:
                    return moves

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if not (0 <= nr < m and 0 <= nc < n):
                        continue

                    if classroom[nr][nc] == 'X':
                        continue

                    ne = e - 1

                    if ne < 0:
                        continue

                    nmask = mask

                    # Pick up litter
                    if (nr, nc) in litter:
                        nmask |= 1 << litter[(nr, nc)]

                    # Recharge energy
                    if classroom[nr][nc] == 'R':
                        ne = energy

                    state = (nr, nc, ne, nmask)

                    if state not in visited:
                        visited.add(state)
                        q.append(state)

            moves += 1

        return -1