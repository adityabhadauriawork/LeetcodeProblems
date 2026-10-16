class Solution:
    def sumCounts(self, nums: list[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        
        tree_sum = [0] * (4 * n)
        tree_sq_sum = [0] * (4 * n)
        lazy = [0] * (4 * n)
        
        def push_down(node, start, end):
            if lazy[node] == 0:
                return
            
            val = lazy[node]
            mid = (start + end) // 2
            left, right = 2 * node, 2 * node + 1
            
            left_len = mid - start + 1
            tree_sq_sum[left] = (tree_sq_sum[left] + 2 * val * tree_sum[left] + val * val * left_len) % MOD
            tree_sum[left] = (tree_sum[left] + val * left_len) % MOD
            lazy[left] += val
            
            right_len = end - mid
            tree_sq_sum[right] = (tree_sq_sum[right] + 2 * val * tree_sum[right] + val * val * right_len) % MOD
            tree_sum[right] = (tree_sum[right] + val * right_len) % MOD
            lazy[right] += val
            
            lazy[node] = 0

        def update(node, start, end, l, r, val):
            if l <= start and end <= r:
                segment_len = end - start + 1
                tree_sq_sum[node] = (tree_sq_sum[node] + 2 * val * tree_sum[node] + val * val * segment_len) % MOD
                tree_sum[node] = (tree_sum[node] + val * segment_len) % MOD
                lazy[node] += val
                return
            
            push_down(node, start, end)
            mid = (start + end) // 2
            if l <= mid:
                update(2 * node, start, mid, l, r, val)
            if r > mid:
                update(2 * node + 1, mid + 1, end, l, r, val)
                
            tree_sum[node] = (tree_sum[2 * node] + tree_sum[2 * node + 1]) % MOD
            tree_sq_sum[node] = (tree_sq_sum[2 * node] + tree_sq_sum[2 * node + 1]) % MOD

        total_ans = 0
        last_seen = {}
        
        for r, num in enumerate(nums):
            l = last_seen.get(num, -1) + 1
            update(1, 0, n - 1, l, r, 1)
            last_seen[num] = r
            total_ans = (total_ans + tree_sq_sum[1]) % MOD
            
        return total_ans
