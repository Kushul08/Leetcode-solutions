# ─────────────────────────────────────────────────
#  Problem : 1192. Critical Connections in a Network
#  Difficulty : Hard
#  Runtime  : 222 ms
#  Memory   : 93.4 MB
#  Solved   : 2026-07-21
# ─────────────────────────────────────────────────

class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        adj_list=[[] for _ in range(n)]
        for u,v in connections:
            adj_list[u].append(v)
            adj_list[v].append(u)
        visited=[0]*n
        bridges=[]
        timer=1
        low=[0]*n
        tin=[0]*n   
        def dfs(node,parent,low,tin):
            nonlocal timer
            visited[node]=1
            low[node]=timer
            tin[node]=timer
            timer+=1
            for it in adj_list[node]:
                if it==parent: continue
                if visited[it]==0:
                    dfs(it,node,low,tin)
                    low[node]=min(low[node],low[it])
                    if low[it]>tin[node]:# why i am here comapring the low of it with the tin of node
                        bridges.append([node,it])
                else:
                    low[node]=min(low[node],low[it])
        dfs(0,-1,low,tin)
        return bridges