# ─────────────────────────────────────────────────
#  Problem : 0094. Binary Tree Inorder Traversal
#  Difficulty : Easy
#  Runtime  : 0 ms
#  Memory   : 12.3 MB
#  Solved   : 2026-05-18
# ─────────────────────────────────────────────────

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        nums=[]
        def inorder(root):
            if not root:
                return []
            inorder(root.left)
            nums.append(root.val)
            inorder(root.right)
            return nums
        return inorder(root)