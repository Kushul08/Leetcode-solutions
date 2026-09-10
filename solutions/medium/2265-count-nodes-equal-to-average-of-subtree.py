# ─────────────────────────────────────────────────
#  Problem : 2265. Count Nodes Equal to Average of Subtree
#  Difficulty : Medium
#  Runtime  : 34 ms
#  Memory   : 14 MB
#  Solved   : 2026-09-10
# ─────────────────────────────────────────────────

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def averageOfSubtree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        ans=[0]
        def recur(node):
            if not node:
                return 0,0
            
            lsum,nl=recur(node.left)
            rsum,nr=recur(node.right)

            if (node.val+lsum+rsum)//(nl+nr+1)==node.val:
                ans[0]+=1
            return (node.val+lsum+rsum),(nl+nr+1)
        recur(root)
        return ans[0]