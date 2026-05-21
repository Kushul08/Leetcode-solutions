# ─────────────────────────────────────────────────
#  Problem : 0235. Lowest Common Ancestor of a Binary Search Tree
#  Difficulty : Medium
#  Runtime  : 54 ms
#  Memory   : 20.4 MB
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

        while root:
            if p.val<root.val and q.val<root.val:
                root=root.left
            elif p.val>root.val and q.val>root.val:
                root=root.right
            else:
                return root
        