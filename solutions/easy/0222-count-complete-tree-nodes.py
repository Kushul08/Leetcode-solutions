# ─────────────────────────────────────────────────
#  Problem : 0222. Count Complete Tree Nodes
#  Difficulty : Easy
#  Runtime  : 39 ms
#  Memory   : 28.4 MB
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
            if not root:
                return 0
            return 1+left_height(root.left)
        def right_height(root):
            if not root:
                return 0
            return 1+right_height(root.right)
        def dfs(root):
            if not root:
                return 0
            
            left=left_height(root)
            right=right_height(root.right)

            if left==right:
                return pow(2,left)-1
            else:
                return 1+dfs(root.left)+dfs(root.right)
        return dfs(root)