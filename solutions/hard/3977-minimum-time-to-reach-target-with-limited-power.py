# ─────────────────────────────────────────────────
#  Problem : 3977. Minimum Time to Reach Target With Limited Power
#  Difficulty : Hard
#  Runtime  : 5983 ms
#  Memory   : 40.9 MB
#  Solved   : 2026-06-28
# ─────────────────────────────────────────────────

from heapq import heappush, heappop
class Solution:
    def minTimeMaxPower(self, n: int, edges: List[List[int]], power: int, cost: List[int], source: int, target: int) -> List[int]:
        n=len(cost)
        if source==target:
            return [0,power]
        adj_list=[[] for _ in range(len(cost))]
        for u,v,t in edges:
            adj_list[u].append((v,t))
        # print(adj_list)
        dist=[[float('inf')]*(power+1) for _ in range(n)]
        dist[source][power]=0

        queue=[]
        heappush(queue,(0,source,power))

        while queue:
            step,node,pow=heappop(queue)
            if step>dist[node][pow]: continue
            for v,c in adj_list[node]:
                curr_pow=pow-cost[node]
                if curr_pow>=0 and step+c<dist[v][curr_pow]:
                    dist[v][curr_pow]=step+c
                    heappush(queue,(step+c,v,curr_pow))
                    # if v==target:
                    #     print(v,steps[v],rem_pow[v])
        min_steps=min(dist[target])
        power_left=0
        for i,step in enumerate(dist[target]):
            if step==min_steps:
                power_left=max(power_left,i)
        if min_steps==float('inf'):
            return [-1,-1]
        return [min_steps,power_left]