# ─────────────────────────────────────────────────
#  Problem : 1732. Find the Highest Altitude
#  Difficulty : Easy
#  Runtime  : 0 ms
#  Memory   : 12.5 MB
#  Solved   : 2026-06-19
# ─────────────────────────────────────────────────

class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        prefix_sum=0
        high=0
        for altitude in gain:
            prefix_sum+=altitude
            high=max(high,prefix_sum)
        
        return high