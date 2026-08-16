# ─────────────────────────────────────────────────
#  Problem : 4020. Elevator Requests I
#  Difficulty : Easy
#  Runtime  : 2 ms
#  Memory   : 12.4 MB
#  Solved   : 2026-08-16
# ─────────────────────────────────────────────────

class Solution(object):
    def elevatorRequests(self, n, requests):
        """
        :type n: int
        :type requests: List[int]
        :rtype: int
        """
        time=0
        curr=0
        for request in requests:
            time+=abs(request-curr)
            curr=request
        return time