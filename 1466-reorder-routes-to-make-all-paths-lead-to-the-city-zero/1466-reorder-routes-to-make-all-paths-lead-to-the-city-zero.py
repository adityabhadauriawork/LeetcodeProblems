from typing import List
from collections import defaultdict

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = defaultdict(list)

        for u, v in connections:
            graph[u].append((v, 1))  # Original direction (needs reversal if used)
            graph[v].append((u, 0))  # Reverse edge (already points correctly)

        visited = set()
        count = 0

        def dfs(node):
            nonlocal count
            visited.add(node)

            for nei, needs_reverse in graph[node]:
                if nei not in visited:
                    count += needs_reverse
                    dfs(nei)

        dfs(0)
        return count