# ─────────────────────────────────────────────────
#  Problem : 3161. Block Placement Queries
#  Difficulty : Hard
#  Runtime  : 0 ms
#  Memory   : 12.5 MB
#  Solved   : 2026-05-30
# ─────────────────────────────────────────────────

from bisect import bisect_left, bisect_right, insort 
class Solution(object):
    def getResults(self, queries):
        """
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        obstacles=[]
        ans=[]

        for q in queries:
            if q[0]==1:
                x=q[1]
                insort(obstacles,q[1])
            else:
                _,x,sz=q

                indx=bisect_right(obstacles,x)

                prev=0
                max_gap=0
                for i in range(indx):
                    max_gap=max(max_gap,obstacles[i]-prev)
                    prev=obstacles[i]
                max_gap=max(max_gap,x-prev)

                ans.append(max_gap>=sz)
        return ans