# ─────────────────────────────────────────────────
#  Problem : 1288. Remove Covered Intervals
#  Difficulty : Medium
#  Runtime  : 0 ms
#  Memory   : 12.6 MB
#  Solved   : 2026-07-06
# ─────────────────────────────────────────────────

class Solution(object):
    def removeCoveredIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals.sort()
        last=None
        count=0
        for interval in intervals:
            if count and last[0]<=interval[0] and last[1]>=interval[1]:
                continue
            elif count and last[0]==interval[0] and last[1]<interval[1]:
                last=interval
            else:
                last=(interval)
                count+=1
        return count