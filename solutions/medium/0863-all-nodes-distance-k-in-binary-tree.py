# ─────────────────────────────────────────────────
#  Problem : 0863. All Nodes Distance K in Binary Tree
#  Difficulty : Medium
#  Runtime  : 20 ms
#  Memory   : 12.5 MB
#  Solved   : 2026-05-15
# ─────────────────────────────────────────────────

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
class Solution(object):
    def distanceK(self, root, target, k):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type k: int
        :rtype: List[int]
        """
        parent={}
        queue=deque([root])
        
        while queue:
            node=queue.popleft()
            if node.left:
                parent[node.left]=node
                queue.append(node.left)
            if node.right:
                parent[node.right]=node
                queue.append(node.right)
        d=0
        visited=set()
        visited.add(target.val)
        queue=deque([target])
        size=len(queue)
        while d<k and queue:
            node=queue.popleft()
            if node in parent and parent[node].val not in visited:
                queue.append(parent[node])
                visited.add(parent[node].val)
            if node.left and node.left.val not in visited:
                queue.append(node.left)
                visited.add(node.left.val)
            if node.right and node.right.val not in visited:
                queue.append(node.right)
                visited.add(node.right.val)
            size-=1
            if size==0:
                d+=1
                size=len(queue)
        ans=[]
        while queue:
            node=queue.popleft()
            ans.append(node.val)
        return ans
