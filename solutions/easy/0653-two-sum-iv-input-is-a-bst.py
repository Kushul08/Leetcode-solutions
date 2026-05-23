# ─────────────────────────────────────────────────
#  Problem : 0653. Two Sum IV - Input is a BST
#  Difficulty : Easy
#  Runtime  : 15 ms
#  Memory   : 18.5 MB
#  Solved   : 2026-05-23
# ─────────────────────────────────────────────────

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: bool
        """
        hashmap=set()

        def recursive(root,hashmap,k):
            if not root:
                return False
            if (k-root.val) in hashmap:
                return True
            hashmap.add(root.val)

            left=recursive(root.left,hashmap,k)
            right=recursive(root.right,hashmap,k)
            return left or right
        return recursive(root,hashmap,k)