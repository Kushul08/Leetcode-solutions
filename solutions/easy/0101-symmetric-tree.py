# ─────────────────────────────────────────────────
#  Problem : 0101. Symmetric Tree
#  Difficulty : Easy
#  Runtime  : 0 ms
#  Memory   : 12.5 MB
#  Solved   : 2026-09-04
# ─────────────────────────────────────────────────

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def dfs(root1,root2):
            if not root1 and not root2: return True
            if not root1 or not root2: return False
            # print(root1.val,root2.val)
            if root1.val==root2.val and dfs(root1.left,root2.right) and dfs(root1.right,root2.left):
                return True
            else:
                return False
        return dfs(root,root)