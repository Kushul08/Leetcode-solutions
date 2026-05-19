# ─────────────────────────────────────────────────
#  Problem : 0700. Search in a Binary Search Tree
#  Difficulty : Easy
#  Runtime  : 0 ms
#  Memory   : 16.4 MB
#  Solved   : 2026-05-19
# ─────────────────────────────────────────────────

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: Optional[TreeNode]
        :type val: int
        :rtype: Optional[TreeNode]
        """
        node=root
        while node:
            if node.val==val:
                return node
            elif val<node.val:
                node=node.left
            else:
                node=node.right
        return 