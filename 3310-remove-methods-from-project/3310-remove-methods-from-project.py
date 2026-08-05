from collections import deque
from typing import List

class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(n)]
        for u, v in invocations:
            graph[u].append(v)
            
        # Step 1: Find all suspicious methods reachable from k
        suspicious = set([k])
        q = deque([k])
        
        while q:
            curr = q.popleft()
            for nxt in graph[curr]:
                if nxt not in suspicious:
                    suspicious.add(nxt)
                    q.append(nxt)
                    
        # Step 2: Check if any outside method invokes a suspicious method
        for u in range(n):
            if u not in suspicious:
                for v in graph[u]:
                    if v in suspicious:
                        # Outside method invokes a suspicious one, cannot remove any
                        return list(range(n))
                        
        # Step 3: Return remaining non-suspicious methods
        return [i for i in range(n) if i not in suspicious]
