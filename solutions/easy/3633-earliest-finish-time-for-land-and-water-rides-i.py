# ─────────────────────────────────────────────────
#  Problem : 3633. Earliest Finish Time for Land and Water Rides I
#  Difficulty : Easy
#  Runtime  : 47 ms
#  Memory   : 12.5 MB
#  Solved   : 2026-06-03
# ─────────────────────────────────────────────────

from bisect import bisect_right
class Solution(object):
    def earliestFinishTime(self, landStartTime, landDuration, waterStartTime, waterDuration):
        """
        :type landStartTime: List[int]
        :type landDuration: List[int]
        :type waterStartTime: List[int]
        :type waterDuration: List[int]
        :rtype: int
        """
        def solve(first_start,first_dur,sec_start,sec_dur):
            rides=sorted(zip(first_start,first_dur))
            n=len(rides)

            start=[s for s,d in rides]

            prefix=[0]*n
            prefix[0]=rides[0][1]
            for i in range(1,len(rides)):
                prefix[i]=min(prefix[i-1],rides[i][1])
            
            suffix=[0]*n
            suffix[-1]=rides[-1][0]+rides[-1][1]
            for i in range(len(rides)-2,-1,-1):
                suffix[i]=min(suffix[i+1],rides[i][0]+rides[i][1])
            ans=float('inf')
            for s,d in zip(sec_start,sec_dur):
                finish=s+d
                indx=bisect_right(start,finish)
                if indx>0:
                    ans=min(ans,finish+prefix[indx-1])
                if indx<n:
                    ans=min(ans,suffix[indx])
            return ans
        return min(solve(landStartTime, landDuration, waterStartTime, waterDuration),
                    solve(waterStartTime,waterDuration,landStartTime, landDuration))