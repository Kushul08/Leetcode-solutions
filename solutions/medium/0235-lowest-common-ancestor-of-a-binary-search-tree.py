# ─────────────────────────────────────────────────
#  Problem : 0235. Lowest Common Ancestor of a Binary Search Tree
#  Difficulty : Medium
#  Runtime  : 61 ms
#  Memory   : 20.3 MB
#  Solved   : 2026-05-21
# ─────────────────────────────────────────────────

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        node=root

        while node:
            if p.val<node.val and q.val<node.val:
                node=node.left
            elif p.val>node.val and q.val>node.val:
                node=node.right
            else:
                return node
        