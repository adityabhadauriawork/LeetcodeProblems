# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        newnode = TreeNode(target)
        curr = root
        if root is None:
            return newnode
        while  curr!=None:
            #left
            if target<curr.val:
                if curr.left is not None:
                    curr = curr.left
                    
                else:
                    curr.left = newnode
                    break
             #right
            if target>curr.val:
                if curr.right is not None:
                    curr = curr.right
                else:
                    curr.right = newnode
                    break
        return root
            
        