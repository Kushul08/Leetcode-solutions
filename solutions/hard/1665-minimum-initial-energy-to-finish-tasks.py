# ─────────────────────────────────────────────────
#  Problem : 1665. Minimum Initial Energy to Finish Tasks
#  Difficulty : Hard
#  Runtime  : 84 ms
#  Memory   : 47.1 MB
#  Solved   : 2026-05-12
# ─────────────────────────────────────────────────

class Solution(object):
    def minimumEffort(self, tasks):
        """
        :type tasks: List[List[int]]
        :rtype: int
        """
        tasks.sort(key=lambda x:x[1]-x[0],reverse=True)
        ans=0
        energy=0
        for a,m in tasks:
            if ans<m:
                extra=m-ans
                energy+=extra
                ans+=extra
            ans-=a
        return energy