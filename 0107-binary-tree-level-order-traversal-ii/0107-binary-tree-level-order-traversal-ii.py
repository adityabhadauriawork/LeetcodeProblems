# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrderBottom(self, root: TreeNode | None) -> list[list[int]]:
        if root is None:
            return []
        q = deque([root])
        ans = []
        while q:
            lstt=[]
            for _ in range(len(q)):
                ptr = q.popleft()
                lstt.append(ptr.val)
                if ptr.left:
                    q.append(ptr.left)
                if ptr.right:
                    q.append(ptr.right)
            ans.append(lstt)
        return ans[::-1]

        