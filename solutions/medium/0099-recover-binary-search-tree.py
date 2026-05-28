# ─────────────────────────────────────────────────
#  Problem : 0099. Recover Binary Search Tree
#  Difficulty : Medium
#  Runtime  : 12 ms
#  Memory   : 12.7 MB
#  Solved   : 2026-05-28
# ─────────────────────────────────────────────────

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def recoverTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: None Do not return anything, modify root in-place instead.
        """
        first=[None]
        middle=[None]
        second=[None]
        prev=[None]
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            if prev[0] and prev[0].val>node.val:
                if first[0]==None:
                    first[0]=prev[0]
                    middle[0]=node
                else:
                    if second[0]==None:
                        second[0]=node
            prev[0]=node 
            inorder(node.right)
        inorder(root)

        if first[0] and second[0]:
            second[0].val,first[0].val=first[0].val, second[0].val
        else:
            first[0].val,middle[0].val=middle[0].val,first[0].val
        