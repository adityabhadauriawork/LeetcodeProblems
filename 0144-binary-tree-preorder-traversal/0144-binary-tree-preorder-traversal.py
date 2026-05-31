# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans=[]
    def recursive(self, root):
        #base case
        if root is None:
            return None

        self.ans.append(root.val)
        self.recursive(root.left)
        self.recursive(root.right)

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.ans=[]
        self.recursive(root)
        return self.ans
        