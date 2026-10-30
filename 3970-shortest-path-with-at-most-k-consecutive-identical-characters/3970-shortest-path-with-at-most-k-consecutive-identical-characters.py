import heapq

class Solution:
    def shortestPath(self, n: int, edges: list[list[int]], labels: str, k: int) -> int:
        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[u].append((v, w))
        
        dist = [[float('inf')] * (k + 1) for _ in range(n)]
        dist[0][1] = 0
        
        pq = [(0, 0, 1)]
        
        while pq:
            d, u, count = heapq.heappop(pq)
            
            if d > dist[u][count]:
                continue
                
            if u == n - 1:
                return d
                
            for v, w in adj[u]:
                if labels[v] == labels[u]:
                    nc = count + 1
                else:
                    nc = 1
                    
                if nc <= k and d + w < dist[v][nc]:
                    dist[v][nc] = d + w
                    heapq.heappush(pq, (d + w, v, nc))
                    
        ans = min(dist[n - 1])
        return ans if ans != float('inf') else -1
