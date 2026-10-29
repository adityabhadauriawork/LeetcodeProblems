class Solution:
    def isSymmetric(self, root: TreeNode | None) -> bool:
        if not root:
            return True
            
        def helper(root, ptr2):
            
            if root is None and ptr2 is None:
                return True
            if root is None or ptr2 is None:
                return False
            if root.val != ptr2.val:
                return False
            
            return helper(root.left, ptr2.right) and helper(root.right, ptr2.left)
        
        return helper(root.left, root.right)
