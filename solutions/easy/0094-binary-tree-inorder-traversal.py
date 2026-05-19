# ─────────────────────────────────────────────────
#  Problem : 0094. Binary Tree Inorder Traversal
#  Difficulty : Easy
#  Runtime  : 0 ms
#  Memory   : 12.4 MB
#  Solved   : 2026-05-19
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
        inorder=[]
        curr=root

        while curr:
            if curr.left==None:
                inorder.append(curr.val)
                curr=curr.right
            else:
                prev=curr.left
                while prev.right and prev.right!=curr:
                    prev=prev.right
                if  prev.right==None:
                    prev.right=curr
                    curr=curr.left
                else:
                    prev.right=None
                    inorder.append(curr.val)
                    curr=curr.right
        return inorder
