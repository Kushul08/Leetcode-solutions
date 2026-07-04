# ─────────────────────────────────────────────────
#  Problem : 3964. Minimum Lights to Illuminate a Road
#  Difficulty : Medium
#  Runtime  : 798 ms
#  Memory   : 32.1 MB
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
        for i in range(1,len(diff)):
            prefix.append(diff[i]+prefix[-1])
        print(diff,prefix)
        
        

        ans=count=0
        for i,num in enumerate(prefix):
            if i==len(prefix)-1: break
            if num==0:
                count+=1
            else:
                print(count)
                ans+=math.ceil(count/3)
                count=0
        if count:
            ans+=math.ceil(count/3)
        return ans