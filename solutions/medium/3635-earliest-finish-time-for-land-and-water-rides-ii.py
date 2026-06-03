# ─────────────────────────────────────────────────
#  Problem : 3635. Earliest Finish Time for Land and Water Rides II
#  Difficulty : Medium
#  Runtime  : 1244 ms
#  Memory   : 31.5 MB
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
        def solve(firststart,firstdur,secondstart,seconddur):

            rides=sorted(zip(secondstart,seconddur))

            start=[s for s,d in rides]
            n=len(start)

            prefix=[0]*n
            prefix[0]=rides[0][-1]
            for i in range(1,len(rides)):
                prefix[i]=min(prefix[i-1],rides[i][-1])
            
            suffix=[0]*n
            suffix[-1]=rides[-1][0]+rides[-1][-1]

            for i in range(len(rides)-2,-1,-1):
                suffix[i]=min(suffix[i+1],rides[i][0]+rides[i][1])
            ans=float('inf')
            for s,d in zip(firststart,firstdur):
                val=s+d
                indx=bisect_right(start,val)

                if indx>0:
                    ans=min(ans,val+prefix[indx-1])
                if indx<n:
                    ans=min(ans,suffix[indx])
            return ans
        
        return min(solve(landStartTime, landDuration, waterStartTime, waterDuration),
                    solve( waterStartTime, waterDuration,landStartTime, landDuration))