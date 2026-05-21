# ─────────────────────────────────────────────────
#  Problem : 0235. Lowest Common Ancestor of a Binary Search Tree
#  Difficulty : Medium
#  Runtime  : 55 ms
#  Memory   : 20.5 MB
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
            node=root
            path=[]
            while node:
                path.append(node)
                if target==node:
                    return path
                if node.val<target.val:
                    node=node.right
                else:
                    node=node.left
        p_path=search(root,p)
        q_path=search(root,q)
        min_len=min(len(p_path),len(q_path))
        for i in range(min_len):
            if p_path[i]!=q_path[i]:
                return last
            last=p_path[i]
        return last