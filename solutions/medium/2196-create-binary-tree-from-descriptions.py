# ─────────────────────────────────────────────────
#  Problem : 2196. Create Binary Tree From Descriptions
#  Difficulty : Medium
#  Runtime  : 324 ms
#  Memory   : 24.6 MB
#  Solved   : 2026-06-07
# ─────────────────────────────────────────────────

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def createBinaryTree(self, descriptions):
        """
        :type descriptions: List[List[int]]
        :rtype: Optional[TreeNode]
        """
        parent=set()
        child=set()
        tree={}
        for p,c,l in descriptions:
            if p not in tree:
                tree[p]=TreeNode(p)
            if c not in tree:
                tree[c]=TreeNode(c)
            if l:
                tree[p].left=tree[c]
            else:
                tree[p].right=tree[c]
            child.add(c)
            if p not in child: parent.add(p)
            if p in child and p in parent: parent.remove(p)
            if c in parent: parent.remove(c)
        return tree[list(parent)[0]]