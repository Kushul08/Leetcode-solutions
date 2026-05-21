# ─────────────────────────────────────────────────
#  Problem : 0235. Lowest Common Ancestor of a Binary Search Tree
#  Difficulty : Medium
#  Runtime  : 15 ms
#  Memory   : 12.5 MB
#  Solved   : 2026-05-21
# ─────────────────────────────────────────────────

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        def search(node,target):
            path
            while node:
                path.append(node.val)
                if p==node:
                    return path
                if node.val<p.val:
                    node=node.right
                else:
                    node=node.left
        p_path=search(root,p)
        q_path=search(root,q)
        print(path)