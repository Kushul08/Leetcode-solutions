# ─────────────────────────────────────────────────
#  Problem : 0099. Recover Binary Search Tree
#  Difficulty : Medium
#  Runtime  : 13 ms
#  Memory   : 12.9 MB
#  Solved   : 2026-05-28
# ─────────────────────────────────────────────────

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def recoverTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: None Do not return anything, modify root in-place instead.
        """
        nums=[]

        def inorder(node):
            if not node:
                return
            inorder(node.left)
            nums.append(node.val)
            inorder(node.right)
        inorder(root)
        nums.sort()
        
        index=[0]
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            if nums[index[0]]!=node.val:
                node.val=nums[index[0]]
            index[0]+=1
            inorder(node.right)
        inorder(root)