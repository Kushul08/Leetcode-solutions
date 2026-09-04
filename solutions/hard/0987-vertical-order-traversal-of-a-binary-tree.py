# ─────────────────────────────────────────────────
#  Problem : 0987. Vertical Order Traversal of a Binary Tree
#  Difficulty : Hard
#  Runtime  : 3 ms
#  Memory   : 19.6 MB
#  Solved   : 2026-09-04
# ─────────────────────────────────────────────────

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        hashmap=defaultdict(list)
        def dfs(root,row,col):
            if not root:
                return
            hashmap[(col,row)].append(root.val)
            if root.left:
                dfs(root.left,row+1,col-1)
            if root.right:
                dfs(root.right,row+1,col+1)
        dfs(root,0,0)
        hashmap=dict(sorted(hashmap.items()))
        prev_col=None
        ans=[]
        for key,val in hashmap.items():
            col,row=key
            if prev_col==None:
                ans.append(val)
            elif prev_col==col:
                ans[-1].extend(sorted(val))
            else:
                ans.append(sorted(val))
            prev_col=col
        return ans