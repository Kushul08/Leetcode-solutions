# ─────────────────────────────────────────────────
#  Problem : 3620. Network Recovery Pathways
#  Difficulty : Hard
#  Runtime  : 0 ms
#  Memory   : 12.5 MB
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
        queue=deque()
        queue.append((0,0,float('inf')))
        costs=[float('inf')]*n
        costs[0]=0
        ans=float('-inf')

        def check(num):
            queue=[]
            heappush(queue,(0,0))

            while queue:
                cost,node=heappop(queue)
                if node==n-1 and cost<=k:
                    return True
                for v,w in adj_list[node]:
                    if w>=num and online[v]==True and cost+w<=k:
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