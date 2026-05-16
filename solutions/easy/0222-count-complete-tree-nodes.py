# ─────────────────────────────────────────────────
#  Problem : 0222. Count Complete Tree Nodes
#  Difficulty : Easy
#  Runtime  : 0 ms
#  Memory   : 28.2 MB
#  Solved   : 2026-05-16
# ─────────────────────────────────────────────────

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def countNodes(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        def left_height(root):
            height=0
            while root:
                height+=1
                root=root.left
            return height
        def right_height(root):
            height=0
            while root:
                height+=1
                root=root.right
            return height
        if not root:
            return 0
            
        left=left_height(root)
        right=right_height(root)

        if left==right:
            return pow(2,left)-1
            
        return 1+self.countNodes(root.left)+self.countNodes(root.right)
        