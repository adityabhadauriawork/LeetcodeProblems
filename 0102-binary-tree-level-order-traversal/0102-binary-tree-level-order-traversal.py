# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if root is None:
            return []
        q = deque([root])
        ans = []
        while q:
            lst=[]
            for _ in range(len(q)):
                ptr = q.popleft()
                lst.append(ptr.val)
                if ptr.left:
                    q.append(ptr.left)
                if ptr.right:
                    q.append(ptr.right)
            ans.append(lst)
        return ans
        