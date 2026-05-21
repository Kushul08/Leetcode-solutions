# ─────────────────────────────────────────────────
#  Problem : 0230. Kth Smallest Element in a BST
#  Difficulty : Medium
#  Runtime  : 23 ms
#  Memory   : 20.2 MB
#  Solved   : 2026-05-21
# ─────────────────────────────────────────────────

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
from sortedcontainers import SortedList
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: int
        """
        nums=SortedList([])
        queue=deque()
        queue.append(root)
        while queue:
            node=queue.popleft()
            nums.add(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return nums[k-1]