# ─────────────────────────────────────────────────
#  Problem : 0222. Count Complete Tree Nodes
#  Difficulty : Easy
#  Runtime  : 0 ms
#  Memory   : 12.5 MB
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
        def dfs(root):
            if not root:
                return 0
            
            left=1+dfs(root.left)
            right=1+dfs(root.right)

            if left==right:
                return pow(2,left)-1
            else:
                return 1+dfs(root.left)+dfs(root.right)
        return dfs(root)