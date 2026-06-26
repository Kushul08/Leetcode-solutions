# ─────────────────────────────────────────────────
#  Problem : 0743. Network Delay Time
#  Difficulty : Medium
#  Runtime  : 356 ms
#  Memory   : 14.5 MB
#  Solved   : 2026-06-26
# ─────────────────────────────────────────────────

from heapq import heappush, heappop
class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        adj_list=[[] for _ in range(n+1)]
        for u,v,w in times:
            adj_list[u].append((v,w))

        queue=[]
        heappush(queue,(0,k))
        signal=[float('inf')]*(n+1)
        signal[k]=0
        while queue:
            dis,node=heappop(queue)
            if dis>signal[node]:
                continue
            for v,w in adj_list[node]:
                if dis+w<signal[v]:
                    signal[v]=dis+w
                    heappush(queue,(signal[v],v))

        ans=float('-inf')
        for i in range(1,len(signal)):
            if signal[i]==float('inf'):
                return -1
            ans=max(ans,signal[i])
            
        return ans if ans!=float('-inf') else -1