# ─────────────────────────────────────────────────
#  Problem : 3964. Minimum Lights to Illuminate a Road
#  Difficulty : Medium
#  Runtime  : 280 ms
#  Memory   : 31.4 MB
#  Solved   : 2026-07-04
# ─────────────────────────────────────────────────

class Solution:
    def minLights(self, lights: list[int]) -> int:
        n=len(lights)
        diff=[0]*(n+1)
        for i,light in enumerate(lights):
            if light:
                l=max(0,i-light)
                r=min(n-1,i+light)
                diff[l]+=1
                diff[r+1]-=1
        prefix=[diff[0]]
        
        curr=0
        ans=count=0
        for i in range(n):
            curr+=diff[i]
            if curr==0:
                count+=1
            else:
                ans+=math.ceil(count/3)
                count=0
        ans+=math.ceil(count/3)
        return ans