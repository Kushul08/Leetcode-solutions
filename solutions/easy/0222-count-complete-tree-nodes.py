# ─────────────────────────────────────────────────
#  Problem : 0222. Count Complete Tree Nodes
#  Difficulty : Easy
#  Runtime  : 7 ms
#  Memory   : 28.3 MB
#  Solved   : 2026-05-16
# ─────────────────────────────────────────────────

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def countNodes(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root: return 0
        queue=deque([root])
        count=0

        while queue:
            node=queue.popleft()
            count+=1
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return count