# ─────────────────────────────────────────────────
#  Problem : 0285. Inorder Successor in BST
#  Difficulty : Medium
#  Runtime  : 42 ms
#  Memory   : 20.5 MB
#  Solved   : 2026-05-23
# ─────────────────────────────────────────────────

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        self.ans=None
        node=root
        while node:
            if p.val<node.val:
                self.ans=node
                node=node.left
            else:
                node=node.right
        return self.ans