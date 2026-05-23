# ─────────────────────────────────────────────────
#  Problem : 0285. Inorder Successor in BST
#  Difficulty : Medium
#  Runtime  : 55 ms
#  Memory   : 20.3 MB
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
        self.ans,self.prev=None,None

        def inorder(node):
            if not node:
                return
            inorder(node.left)
            if self.ans: return 
            if self.prev and self.prev.val==p.val:
                self.ans=node
                return
            self.prev=node
            inorder(node.right)
        inorder(root)
        return self.ans