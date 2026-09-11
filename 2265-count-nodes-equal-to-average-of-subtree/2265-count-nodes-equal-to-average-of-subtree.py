# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        self.matching_nodes_count = 0
        
        def dfs(node):
            if not node:
                # Return (sum_of_values, count_of_nodes)
                return 0, 0
            
            # Post-order traversal: visit left and right subtrees first
            left_sum, left_count = dfs(node.left)
            right_sum, right_count = dfs(node.right)
            
            # Calculate current subtree metrics
            current_sum = left_sum + right_sum + node.val
            current_count = left_count + right_count + 1
            
            # Check if current node value equals the subtree average
            if node.val == (current_sum // current_count):
                self.matching_nodes_count += 1
                
            return current_sum, current_count

        dfs(root)
        return self.matching_nodes_count
