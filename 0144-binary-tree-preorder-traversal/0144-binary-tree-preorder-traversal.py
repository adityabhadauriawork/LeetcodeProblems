# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, value=0, left=None, right=None):
#         self.value = value
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def preorder(root):
            if root is None:
                return
            #this was the base 
            ans.append(root.val)
            preorder(root.left)
            preorder(root.right)
        preorder(root)
        return ans
        