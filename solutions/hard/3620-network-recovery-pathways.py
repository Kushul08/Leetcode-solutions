# ─────────────────────────────────────────────────
#  Problem : 3620. Network Recovery Pathways
#  Difficulty : Hard
#  Runtime  : 52 ms
#  Memory   : 26.2 MB
#  Solved   : 2026-07-03
# ─────────────────────────────────────────────────

from heapq import heappop, heappush
class Solution(object):
    def findMaxPathScore(self, edges, online, k):
        """
        :type edges: List[List[int]]
        :type online: List[bool]
        :type k: int
        :rtype: int
        """
        n=len(online)
        adj_list=[[] for _ in range(n)]
        for u,v,w in edges:
            adj_list[u].append((v,w))
        

        def check(num):
            queue=[]
            heappush(queue,(0,0))
            dis=[float('inf')]*n
            dis[0]=0
            while queue:
                cost,node=heappop(queue)
                if node==n-1:
                    return True
                for v,w in adj_list[node]:
                    if w>=num and online[v]==True and cost+w<=k:
                        if cost+w<dis[v]:
                            dis[v]=cost+w
                            heappush(queue,(cost+w,v))
            return False
        low=0
        high=int(1e9)
        ans=None
        
        while low<=high:
            mid=(low+high)//2
            if check(mid):
                ans=mid
                low=mid+1
            else:
                high=mid-1
        if ans==None:
            return -1
        return ans