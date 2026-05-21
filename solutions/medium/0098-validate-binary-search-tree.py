# ─────────────────────────────────────────────────
#  Problem : 0098. Validate Binary Search Tree
#  Difficulty : Medium
#  Runtime  : 5 ms
#  Memory   : 17.4 MB
#  Solved   : 2026-05-21
# ─────────────────────────────────────────────────

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        prev=[None]
        def inorder(root):
            if not root:
                return True
            
            if not inorder(root.left): return False

            
            if prev[0]!=None and prev[0]>=root.val: return False
            
            prev[0]=root.val
            
            if not inorder(root.right): return False
            return True

        return inorder(root)