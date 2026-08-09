# ─────────────────────────────────────────────────
#  Problem : 4015. Weighted Sum of a Tree
#  Difficulty : Medium
#  Runtime  : 522 ms
#  Memory   : 44.8 MB
#  Solved   : 2026-08-09
# ─────────────────────────────────────────────────

from collections import deque
class Solution(object):
    def weightedSum(self, parent, nums):
        """
        :type parent: List[int]
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        adj_list=[[] for _ in range(n)]
        for i,node in enumerate(parent):
            if i==0: continue
            adj_list[node].append(i)
        
        queue=deque([0])
        depths={0:1}
        depth=2
        temp=[]
        height=1
        while queue:
            node=queue.popleft()
            for nodes in adj_list[node]:
                temp.append(nodes)
                depths[nodes]=depth
                height=max(height,depth)
            if len(queue)==0:
                queue.extend(temp)
                depth+=1
                temp=[]

        weights=0
        for i in range(n):
            weights+=nums[i]*(height-depths[i]+1)
        return weights