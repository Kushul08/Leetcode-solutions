# ─────────────────────────────────────────────────
#  Problem : 1373. Maximum Sum BST in Binary Tree
#  Difficulty : Hard
#  Runtime  : 273 ms
#  Memory   : 83.6 MB
#  Solved   : 2026-05-29
# ─────────────────────────────────────────────────

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxSumBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        max_sum=[0]
        def postorder(node):
            if not node:
                return (0,float('inf'),float('-inf'),True)
            left_sum,left_min,left_max,left_bst=postorder(node.left)
            right_sum,right_min,right_max,right_bst=postorder(node.right)
            
            if (left_bst and left_max<node.val) and (right_bst and node.val<right_min):
                curr_sum=left_sum+right_sum+node.val
                max_sum[0]=max(max_sum[0],curr_sum)
                return (curr_sum,min(left_min,node.val),max(right_max,node.val),True)
            else:
                return (max(left_sum,right_sum),float('-inf'),float('inf'),False)
        postorder(root)
        return max_sum[0]
                 