# ─────────────────────────────────────────────────
#  Problem : 0450. Delete Node in a BST
#  Difficulty : Medium
#  Runtime  : 0 ms
#  Memory   : 20.2 MB
#  Solved   : 2026-05-20
# ─────────────────────────────────────────────────

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: Optional[TreeNode]
        :type key: int
        :rtype: Optional[TreeNode]
        """
        if not root:
            return

        
        
        def last_right(root):
            node=root.left
            prev=node
            while node:
                prev=node
                node=node.right
            return prev

        def helper(root):
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            left_most=last_right(root)
            right_child=root.right
            left_most.right=right_child
            return root.left
        
        if root.val==key:
            return helper(root)
        node=root
        while node:
            if node.val>key:
                if node.left and node.left.val==key:
                    node.left=helper(node.left)
                    break
                else:
                    node=node.left
            else:
                if node.right and node.right.val==key:
                    node.right=helper(node.right)
                    break
                else:
                    node=node.right
        
        return root
        
        