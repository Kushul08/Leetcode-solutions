# ─────────────────────────────────────────────────
#  Problem : 3965. Finish Time of Tasks I
#  Difficulty : Medium
#  Runtime  : 553 ms
#  Memory   : 61 MB
#  Solved   : 2026-07-04
# ─────────────────────────────────────────────────

class Solution(object):
    def finishTime(self, n, edges, baseTime):
        """
        :type n: int
        :type edges: List[List[int]]
        :type baseTime: List[int]
        :rtype: int
        """
        adj_list=[[] for _ in range(n)]
        for u,v in edges:
            adj_list[u].append(v)
        
        stack=[]
        vis=[0]*n

        def dfs(num):
            vis[num]=1
            for neigh in adj_list[num]:
                if vis[num]==0:
                    dfs(neigh)
            stack.append(num)
        for i in range(n):
            if vis[i]==0:
                dfs(i)
        stack=stack[::-1]
        finish_time=[0]*n
        for node in stack:
            if adj_list[node]==[]:
                finish_time[node]=baseTime[node]
                continue
            earliest=float('inf')
            latest=float('-inf')
            for neigh in adj_list[node]:
                earliest=min(earliest,finish_time[neigh])
                latest=max(latest,finish_time[neigh])
            finish_time[node]=(latest-earliest)+baseTime[node]+latest
        return finish_time[stack[-1]]
