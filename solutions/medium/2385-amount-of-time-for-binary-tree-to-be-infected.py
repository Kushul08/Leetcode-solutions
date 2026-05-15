# ─────────────────────────────────────────────────
#  Problem : 2385. Amount of Time for Binary Tree to Be Infected
#  Difficulty : Medium
#  Runtime  : 233 ms
#  Memory   : 95.3 MB
#  Solved   : 2026-05-15
# ─────────────────────────────────────────────────

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def amountOfTime(self, root, start):
        """
        :type root: Optional[TreeNode]
        :type start: int
        :rtype: int
        """
        queue=deque([root])

        parent={}
        Start=None
        while queue:
            node=queue.popleft()
            if node.val==start:
                Start=node
            if node.left:
                parent[node.left]=node
                queue.append(node.left)
            if node.right:
                parent[node.right]=node
                queue.append(node.right)
        queue=deque([Start])
        count=0
        visited=set()
        visited.add(Start)
        size=len(queue)
        while queue:
            node=queue.popleft()
            if node in parent and parent[node] not in visited:
                queue.append(parent[node])
                visited.add(parent[node])
            if node.left and node.left not in visited:
                queue.append(node.left)
                visited.add(node.left)
            if node.right and node.right not in visited:
                queue.append(node.right)
                visited.add(node.right)
            
            size-=1
            if size==0:
                count+=1
                size=len(queue)
        return count-1