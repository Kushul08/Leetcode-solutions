# ─────────────────────────────────────────────────
#  Problem : 1344. Angle Between Hands of a Clock
#  Difficulty : Medium
#  Runtime  : 0 ms
#  Memory   : 12.4 MB
#  Solved   : 2026-06-18
# ─────────────────────────────────────────────────

class Solution(object):
    def angleClock(self, hour, minutes):
        """
        :type hour: int
        :type minutes: int
        :rtype: float
        """
        angle=abs(30*hour-5.5*minutes)
        return min(angle,360-angle)