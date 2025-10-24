# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self,root,k):
        self.count = 0
        self.res = None
        
        def inorder(node):
            if not node:
                return None

            inorder(node.left)
            self.count +=1
            if self.count == k:
                self.res = node.val
                return
            inorder(node.right)
        inorder(root)

        return self.res
        