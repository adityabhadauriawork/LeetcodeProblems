# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        # Helper function to collect leaves via DFS
        def get_leaves(node):
            leaves = []
            
            def dfs(current_node):
                if not current_node:
                    return
                
                # Check if leaf node
                if not current_node.left and not current_node.right:
                    leaves.append(current_node.val)
                
                # Traverse left then right
                dfs(current_node.left)
                dfs(current_node.right)
            
            dfs(node)
            return leaves
        
        # Compare leaf sequences
        return get_leaves(root1) == get_leaves(root2)