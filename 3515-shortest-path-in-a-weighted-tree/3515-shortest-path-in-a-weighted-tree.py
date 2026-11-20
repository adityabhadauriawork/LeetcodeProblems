class Solution:
    def treeQueries(self, n: int, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        adj = collections.defaultdict(list)
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))
            
        tin = [0] * (n + 1)
        tout = [0] * (n + 1)
        dist = [0] * (n + 1)
        edge_w = [0] * (n + 1)
        timer = 0
        
        def dfs(u, p, d):
            nonlocal timer
            timer += 1
            tin[u] = timer
            dist[u] = d
            for v, w in adj[u]:
                if v != p:
                    edge_w[v] = w
                    dfs(v, u, d + w)
            tout[u] = timer

        dfs(1, 0, 0)
        
        bit = [0] * (n + 2)
        def add(i, delta):
            while i <= n:
                bit[i] += delta
                i += i & (-i)
                
        def query(i):
            s = 0
            while i > 0:
                s += bit[i]
                i -= i & (-i)
            return s

        ans = []
        for q in queries:
            if q[0] == 1:
                _, u, v, w = q
                child = v if tin[v] > tin[u] else u
                diff = w - edge_w[child]
                edge_w[child] = w
                add(tin[child], diff)
                add(tout[child] + 1, -diff)
            else:
                x = q[1]
                ans.append(dist[x] + query(tin[x]))
        return ans