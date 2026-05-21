# ─────────────────────────────────────────────────
#  Problem : 0230. Kth Smallest Element in a BST
#  Difficulty : Medium
#  Runtime  : 0 ms
#  Memory   : 20.2 MB
#  Solved   : 2026-05-21
# ─────────────────────────────────────────────────

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: int
        """
        ans=[0]
        count=[0]
        def inorder(node):
            if not node:
                return False

            if inorder(node.left): return True


            count[0]+=1
            if count[0]==k:
                ans[0]=node.val
                return True

            if inorder(node.right): return True

            return False

        inorder(root)
        return ans[-1]