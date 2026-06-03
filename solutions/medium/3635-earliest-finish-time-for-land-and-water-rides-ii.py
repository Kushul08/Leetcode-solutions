# ─────────────────────────────────────────────────
#  Problem : 3635. Earliest Finish Time for Land and Water Rides II
#  Difficulty : Medium
#  Runtime  : 0 ms
#  Memory   : 12.2 MB
#  Solved   : 2026-06-03
# ─────────────────────────────────────────────────

class Solution(object):
    def earliestFinishTime(self, landStartTime, landDuration, waterStartTime, waterDuration):
        """
        :type landStartTime: List[int]
        :type landDuration: List[int]
        :type waterStartTime: List[int]
        :type waterDuration: List[int]
        :rtype: int
        """
        ans=float('inf')
        for i in range(len(landStartTime)):
            for j in range(len(waterStartTime)):
                land=landStartTime[i]+landDuration[i]
                finish1=max(land,waterStartTime[j])+waterDuration[j]

                water=waterStartTime[j]+waterDuration[j]
                finish2=max(water,landStartTime[i])+landDuration[i]

                ans=min(ans,finish1,finish2)
        return ans