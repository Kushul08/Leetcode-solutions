# ─────────────────────────────────────────────────
#  Problem : 3633. Earliest Finish Time for Land and Water Rides I
#  Difficulty : Easy
#  Runtime  : 505 ms
#  Memory   : 12.4 MB
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
                finish1=max(landFinish,waterStartTime[j])+waterDuration[j]

                waterFinish=(waterStartTime[j]+waterDuration[j])
                finish2=max(waterFinish,landStartTime[i])+landDuration[i]

                early_finish=min(early_finish,finish1,finish2)

        return early_finish