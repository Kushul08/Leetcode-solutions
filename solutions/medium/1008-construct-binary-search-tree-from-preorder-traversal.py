# ─────────────────────────────────────────────────
#  Problem : 1008. Construct Binary Search Tree from Preorder Traversal
#  Difficulty : Medium
#  Runtime  : 1 ms
#  Memory   : 12.7 MB
#  Solved   : 2026-05-23
# ─────────────────────────────────────────────────

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: Optional[TreeNode]
        """
        self.i=0
        def construct(i,upper_bound):
            if self.i==len(preorder) or preorder[self.i]>upper_bound:
                return None
            root=TreeNode(preorder[self.i])
            self.i+=1
            root.left=construct(self.i,root.val)
            root.right=construct(self.i,upper_bound)
            return root
        return construct(0,float('inf'))