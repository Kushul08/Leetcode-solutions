# ─────────────────────────────────────────────────
#  Problem : 3633. Earliest Finish Time for Land and Water Rides I
#  Difficulty : Easy
#  Runtime  : 603 ms
#  Memory   : 12.3 MB
#  Solved   : 2026-06-02
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
        early_finish=float('inf')

        for i in range(len(landStartTime)):
            for j in range(len(waterStartTime)):
                landFinish=(landStartTime[i]+landDuration[i])
                early_finish=min(early_finish,max(landFinish,waterStartTime[j])+waterDuration[j])
        

        for i in range(len(waterStartTime)):
            for j in range(len(landStartTime)):
                waterFinish=(waterStartTime[i]+waterDuration[i])
                early_finish=min(early_finish,max(waterFinish,landStartTime[j])+landDuration[j])
        return early_finish