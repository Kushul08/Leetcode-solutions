# ─────────────────────────────────────────────────
#  Problem : 0230. Kth Smallest Element in a BST
#  Difficulty : Medium
#  Runtime  : 6 ms
#  Memory   : 20.4 MB
#  Solved   : 2026-05-21
# ─────────────────────────────────────────────────

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: int
        """
        ans=[0]
        count=[0]
        def inorder(node):
            if not node:
                return 
            inorder(node.left)
            count[0]+=1
            if count[0]==k:
                ans[0]=node.val
            inorder(node.right)
            return ans[0]
        return inorder(root)