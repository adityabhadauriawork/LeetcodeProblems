class Solution:
    def isBalanced(self, root: TreeNode | None) -> bool:

        def helper(node):
            if node is None:
                return 0

            left_height = helper(node.left)
            if left_height == -1:
                return -1

            right_height = helper(node.right)
            if right_height == -1:
                return -1

            if abs(left_height - right_height) > 1:
                return -1

            return 1 + max(left_height, right_height)
            return 

        return helper(root) != -1

        