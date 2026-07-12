# ─────────────────────────────────────────────────
#  Problem : 3986. Number of Elapsed Seconds Between Two Times
#  Difficulty : Easy
#  Runtime  : 0 ms
#  Memory   : 12.4 MB
#  Solved   : 2026-07-12
# ─────────────────────────────────────────────────

class Solution(object):
    def secondsBetweenTimes(self, startTime, endTime):
        """
        :type startTime: str
        :type endTime: str
        :rtype: int
        """
        h1=int(startTime[:2])
        # print(h1)
        h2=int(endTime[:2])
        m1=int(startTime[3:5])
        m2=int(endTime[3:5])

        s1=int(startTime[6:8])
        s2=int(endTime[6:8])
        
        return ((h2*3600+m2*60+s2)-(h1*3600+m1*60+s1))