class Node:
    def __init__(self, k: int):
        self.remain = [0] * k
        self.prod = 1

class Solution:
    def resultArray(self, nums: list[int], k: int, queries: list[list[int]]) -> list[int]:
        n = len(nums)
        nums_mod = [x % k for x in nums]
        
        # Merge function for segment tree nodes
        def merge(left: Node, right: Node) -> Node:
            res = Node(k)
            res.prod = (left.prod * right.prod) % k
            for r in range(k):
                res.remain[r] = left.remain[r]
            # Combine left residues with right residues shifted by left.prod
            for r in range(k):
                new_r = (left.prod * r) % k
                res.remain[new_r] += right.remain[r]
            return res

        tree = [Node(k) for _ in range(4 * n)]

        def build(idx: int, l: int, r: int):
            if l == r:
            # Base leaf node
                tree[idx].remain[nums_mod[l]] = 1
                tree[idx].prod = nums_mod[l]
                return
            mid = (l + r) // 2
            build(2 * idx, l, mid)
            build(2 * idx + 1, mid + 1, r)
            tree[idx] = merge(tree[2 * idx], tree[2 * idx + 1])

        def update(idx: int, l: int, r: int, pos: int, val: int):
            if l == r:
                tree[idx].remain = [0] * k
                tree[idx].remain[val] = 1
                tree[idx].prod = val
                return
            mid = (l + r) // 2
            if pos <= mid:
                update(2 * idx, l, mid, pos, val)
            else:
                update(2 * idx + 1, mid + 1, r, pos, val)
            tree[idx] = merge(tree[2 * idx], tree[2 * idx + 1])

        def query(idx: int, l: int, r: int, ql: int, qr: int) -> Node:
            if ql <= l and r <= qr:
                return tree[idx]
            mid = (l + r) // 2
            if qr <= mid:
                return query(2 * idx, l, mid, ql, qr)
            if ql > mid:
                return query(2 * idx + 1, mid + 1, r, ql, qr)
            return merge(query(2 * idx, l, mid, ql, qr), query(2 * idx + 1, mid + 1, r, ql, qr))

        build(1, 0, n - 1)
        ans = []
        for index_i, value_i, start_i, xi in queries:
            val_mod = value_i % k
            update(1, 0, n - 1, index_i, val_mod)
            nums_mod[index_i] = val_mod
            node_res = query(1, 0, n - 1, start_i, n - 1)
            ans.append(node_res.remain[xi])
            
        return ans
