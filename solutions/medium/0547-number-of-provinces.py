# ─────────────────────────────────────────────────
#  Problem : 0547. Number of Provinces
#  Difficulty : Medium
#  Runtime  : 8 ms
#  Memory   : 13 MB
#  Solved   : 2026-05-31
# ─────────────────────────────────────────────────

from collections import deque
class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        n=len(isConnected)
        count=0
        adj_list={i:[] for i in range(1,n+1)}
        for i in range(len(isConnected)):
            for j in range(len(isConnected[i])):
                if isConnected[i][j]!=0:
                    adj_list[i+1].append(j+1)



        seen=set()
        for i in range(1,n+1):
            if i in seen:
                continue
            seen.add(i)
            queue=deque([i])
                
            while queue:
                node=queue.popleft()
                for neighbour in adj_list[node]:
                    if neighbour not in seen:
                        seen.add(neighbour)
                        queue.append(neighbour)

            count+=1
        return count