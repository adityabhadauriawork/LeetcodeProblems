from typing import List
from collections import defaultdict

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        graph = defaultdict(list)

        # Build graph
        for (a, b), value in zip(equations, values):
            graph[a].append((b, value))
            graph[b].append((a, 1 / value))

        def dfs(src, dest, visited):
            if src == dest:
                return 1.0

            visited.add(src)

            for neighbor, weight in graph[src]:
                if neighbor not in visited:
                    result = dfs(neighbor, dest, visited)
                    if result != -1:
                        return weight * result

            return -1

        ans = []

        for src, dest in queries:

            if src not in graph or dest not in graph:
                ans.append(-1.0)

            else:
                ans.append(dfs(src, dest, set()))

        return ans