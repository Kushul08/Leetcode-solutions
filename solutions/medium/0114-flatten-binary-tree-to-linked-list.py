# ─────────────────────────────────────────────────
#  Problem : 0114. Flatten Binary Tree to Linked List
#  Difficulty : Medium
#  Runtime  : 0 ms
#  Memory   : 12.6 MB
#  Solved   : 2026-05-19
# ─────────────────────────────────────────────────

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flatten(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: None Do not return anything, modify root in-place instead.
        """
        prev=[None]
        def recursive(node):
            if not node:
                return
            recursive(node.right)
            recursive(node.left)
            node.right=prev[0]
            node.left=None
            prev[0]=node
        recursive(root)
