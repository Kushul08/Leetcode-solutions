# ─────────────────────────────────────────────────
#  Problem : 0701. Insert into a Binary Search Tree
#  Difficulty : Medium
#  Runtime  : 0 ms
#  Memory   : 16.6 MB
#  Solved   : 2026-05-20
# ─────────────────────────────────────────────────

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: Optional[TreeNode]
        :type val: int
        :rtype: Optional[TreeNode]
        """
        if not root:
            return TreeNode(val)
        node=root
        prev=root
        while node:
            if node.val<val:
                prev=node
                node=node.right
            else:
                prev=node
                node=node.left
        if val>prev.val:
            prev.right=TreeNode(val)
        else:
            prev.left=TreeNode(val)
        return root