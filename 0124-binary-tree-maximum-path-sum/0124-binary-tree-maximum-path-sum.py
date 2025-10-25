# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxi = root.val

        def dfs(root):
            nonlocal maxi
            if not root:
                return 0
            l = dfs(root.left)
            r = dfs(root.right)
            maxi = max(maxi, root.val, l+r+root.val , root.val+l , root.val+r)
            return max(root.val, l+root.val, r+root.val)
        dfs(root)
        return maxi
            