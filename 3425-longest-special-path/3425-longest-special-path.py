class Solution:
    def longestSpecialPath(self, edges: List[List[int]], nums: List[int]) -> List[int]:
        n = len(nums)
        adj = collections.defaultdict(list)
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))
            
        ans = [0, 1]
        prefix = [0]
        last_seen = {}
        
        def dfs(u, p, left_bound):
            val = nums[u]
            prev_depth = last_seen.get(val, -1)
            new_left = max(left_bound, prev_depth + 1)
            
            cur_len = prefix[-1] - prefix[new_left]
            cur_nodes = len(prefix) - new_left
            
            if cur_len > ans[0] or (cur_len == ans[0] and cur_nodes < ans[1]):
                ans[0] = cur_len
                ans[1] = cur_nodes
                
            last_seen[val] = len(prefix) - 1
            for v, w in adj[u]:
                if v != p:
                    prefix.append(prefix[-1] + w)
                    dfs(v, u, new_left)
                    prefix.pop()
                    
            if prev_depth == -1:
                del last_seen[val]
            else:
                last_seen[val] = prev_depth

        dfs(0, -1, 0)
        return ans