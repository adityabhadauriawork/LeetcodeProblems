# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = True
    def height(self,root):
        if root is None:
            return 0
        leftmax = self.height(root.left)
        rightmax = self.height(root.right)
        if abs(leftmax - rightmax) > 1:
            self.ans = False
        return (max(leftmax,rightmax)+1)
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.height(root)
        return self.ans
        
       

        
        