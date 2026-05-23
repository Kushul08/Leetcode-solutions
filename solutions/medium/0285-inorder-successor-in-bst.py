# ─────────────────────────────────────────────────
#  Problem : 0285. Inorder Successor in BST
#  Difficulty : Medium
#  Runtime  : 15 ms
#  Memory   : 12.4 MB
#  Solved   : 2026-05-23
# ─────────────────────────────────────────────────

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        nums=[]
        index=[0]
        def inorder(root):
            if not root:
                return
            if root==p:
                index[0]=len(nums)
            inorder(root.left)
            nums.append(root)
            inorder(root.right)
        inorder(root)
        return nums[index[0]+1]