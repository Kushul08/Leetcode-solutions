# ─────────────────────────────────────────────────
#  Problem : 1288. Remove Covered Intervals
#  Difficulty : Medium
#  Runtime  : 0 ms
#  Memory   : 12.3 MB
#  Solved   : 2026-07-06
# ─────────────────────────────────────────────────

class Solution(object):
    def removeCoveredIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals.sort()
        stack=[]
        for interval in intervals:
            if stack and stack[-1][0]<=interval[0] and stack[-1][1]>=interval[1]:
                continue
            else:
                stack.append(interval)
        return len(stack)