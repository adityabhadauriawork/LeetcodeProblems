# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def depth(root):
            # base case
            if root is None:
                return 0
            #leaf node is reached
            if root.left is None and root.right is None:
                return 1
            #only left
            if root.right is None:
                return 1 + depth(root.left)
            #only right
            if root.left is None:
                return 1 + depth(root.right)
            #both are present then
            left_depth = depth(root.left)
            right_depth = depth(root.right)
            # now return if both are present
            return 1 + min(left_depth, right_depth)
        return depth(root)
        