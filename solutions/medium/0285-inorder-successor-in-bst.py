# ─────────────────────────────────────────────────
#  Problem : 0285. Inorder Successor in BST
#  Difficulty : Medium
#  Runtime  : 18 ms
#  Memory   : 12.4 MB
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
        self.prev=None

        def inorder(node):
            if not node or self.ans:
                return
            inorder(node.left)

            if self.prev==p:
                self.ans=node
                return 
            self.prev=node

            inorder(node.right)

        inorder(root)
        return self.ans
