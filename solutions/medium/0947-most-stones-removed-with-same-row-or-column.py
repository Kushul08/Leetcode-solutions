# ─────────────────────────────────────────────────
#  Problem : 0947. Most Stones Removed with Same Row or Column
#  Difficulty : Medium
#  Runtime  : 845 ms
#  Memory   : 12.9 MB
#  Solved   : 2026-09-05
# ─────────────────────────────────────────────────

class DSU:
    def __init__(self,query):
        self.parent={}
        self.rank={}
        for x,y in query:
            self.parent[(x,y)]=(x,y)
            self.rank[(x,y)]=0
    def find_par(self,(x,y)):
        if self.parent[(x,y)]==(x,y):
            return (x,y)
        #print(x,y,self.parent[(x,y)])
        self.parent[(x,y)]=self.find_par(self.parent[(x,y)])
        return self.parent[(x,y)]
    def union(self,x,y,u,v):
        ulp_u=self.find_par((x,y))
        ulp_v=self.find_par((u,v))
        if ulp_u==ulp_v:
            return
        if self.rank[(ulp_u)]<self.rank[ulp_v]:
            self.parent[ulp_u]=ulp_v
        elif self.rank[ulp_u]>self.rank[ulp_v]:
            self.parent[ulp_v]=ulp_u
        else:
            self.parent[ulp_v]=ulp_u
            self.rank[ulp_u]+=1
        
    
class Solution(object):
    def removeStones(self, stones):
        """
        :type stones: List[List[int]]
        :rtype: int
        """
        n=len(stones)
        dsu=DSU(stones)
        components=0
        for i in range(n):
            x,y=stones[i][0],stones[i][1]
            for j in range(i+1,n):
                u,v=stones[j][0],stones[j][1]
                if x==u or y==v:
                    dsu.union(x,y,u,v)
        #print(dsu.parent)
        parent=dsu.parent
        components=set()
        for x,y in stones:
            if dsu.find_par((x,y)) not in components:
                components.add(dsu.parent[(x,y)])
        return n-len(components)