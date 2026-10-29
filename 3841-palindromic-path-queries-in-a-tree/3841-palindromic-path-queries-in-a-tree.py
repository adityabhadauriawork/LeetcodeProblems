import sys

sys.setrecursionlimit(200000)

class Solution:
    def palindromePath(self, n: int, edges: list[list[int]], s: str, queries: list[str]) -> list[bool]:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        parent = [0] * n
        depth = [0] * n
        size = [0] * n
        heavy = [-1] * n
        
        def dfs_sz(u, p, d):
            parent[u] = p
            depth[u] = d
            size[u] = 1
            max_s = 0
            for v in adj[u]:
                if v != p:
                    dfs_sz(v, u, d + 1)
                    size[u] += size[v]
                    if size[v] > max_s:
                        max_s = size[v]
                        heavy[u] = v
                        
        dfs_sz(0, -1, 0)
        
        head = [0] * n
        pos = [0] * n
        cur_pos = 0
        
        def dfs_hld(u, h):
            nonlocal cur_pos
            head[u] = h
            pos[u] = cur_pos
            cur_pos += 1
            if heavy[u] != -1:
                dfs_hld(heavy[u], h)
            for v in adj[u]:
                if v != parent[u] and v != heavy[u]:
                    dfs_hld(v, v)
                    
        dfs_hld(0, 0)
        
        tree = [0] * (4 * n)
        
        def build(node, start, end):
            if start == end:
                return
            mid = (start + end) // 2
            build(2 * node, start, mid)
            build(2 * node + 1, mid + 1, end)
            
        build(1, 0, n - 1)
        
        def update_tree(node, start, end, idx, val):
            if start == end:
                tree[node] = val
                return
            mid = (start + end) // 2
            if start <= idx <= mid:
                update_tree(2 * node, start, mid, idx, val)
            else:
                update_tree(2 * node + 1, mid + 1, end, idx, val)
            tree[node] = tree[2 * node] ^ tree[2 * node + 1]
            
        def query_tree(node, start, end, l, r):
            if r < start or end < l:
                return 0
            if l <= start and end <= r:
                return tree[node]
            mid = (start + end) // 2
            p1 = query_tree(2 * node, start, mid, l, r)
            p2 = query_tree(2 * node + 1, mid + 1, end, l, r)
            return p1 ^ p2
            
        for i in range(n):
            val = 1 << (ord(s[i]) - ord('a'))
            update_tree(1, 0, n - 1, pos[i], val)
            
        ans = []
        for q in queries:
            parts = q.split()
            if parts[0] == "update":
                u = int(parts[1])
                c = parts[2]
                val = 1 << (ord(c) - ord('a'))
                update_tree(1, 0, n - 1, pos[u], val)
            else:
                u = int(parts[1])
                v = int(parts[2])
                res = 0
                while head[u] != head[v]:
                    if depth[head[u]] > depth[head[v]]:
                        u, v = v, u
                    res ^= query_tree(1, 0, n - 1, pos[head[v]], pos[v])
                    v = parent[head[v]]
                if depth[u] > depth[v]:
                    u, v = v, u
                res ^= query_tree(1, 0, n - 1, pos[u], pos[v])
                ans.append((res & (res - 1)) == 0)
                
        return ans
