import collections

class Solution:
    def canMerge(self, trees: list[TreeNode]) -> TreeNode | None:
        nodes = {t.val: t for t in trees}
        freq = collections.Counter(v for t in trees for v in ([t.val] + ([t.left.val] if t.left else []) + ([t.right.val] if t.right else [])))
        
        def validate(node, low=float('-inf'), high=float('inf')):
            if not node: return True
            if not (low < node.val < high): return False
            if not node.left and not node.right and node.val in nodes and node.val != root_val:
                child = nodes.pop(node.val)
                node.left, node.right = child.left, child.right
            return validate(node.left, low, node.val) and validate(node.right, node.val, high)

        for t in trees:
            if freq[t.val] == 1:
                root_val = t.val
                if validate(t) and len(nodes) == 1:
                    return t
        return trees[0] if len(trees) == 1 else None
