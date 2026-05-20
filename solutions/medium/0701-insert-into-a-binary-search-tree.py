# ─────────────────────────────────────────────────
#  Problem : 0701. Insert into a Binary Search Tree
#  Difficulty : Medium
#  Runtime  : 4 ms
#  Memory   : 16.5 MB
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
        if not node:
            new_node=TreeNode(val)
            if val>prev.val:
                prev.right=new_node
            else:
                prev.left=new_node
        return root