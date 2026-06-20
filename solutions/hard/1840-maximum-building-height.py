# ─────────────────────────────────────────────────
#  Problem : 1840. Maximum Building Height
#  Difficulty : Hard
#  Runtime  : 506 ms
#  Memory   : 38.3 MB
#  Solved   : 2026-06-20
# ─────────────────────────────────────────────────

class Solution(object):
    def maxBuilding(self, n, restrictions):
        """
        :type n: int
        :type restrictions: List[List[int]]
        :rtype: int
        """
        restrictions.append([1,0])
        restrictions.append([n,n-1])
        restrictions.sort()
        max_height=0
        for i in range(len(restrictions)-1):
            distance=restrictions[i+1][0]-restrictions[i][0]
            current=restrictions[i][1]+distance
            restrictions[i+1][1]=min(restrictions[i+1][1],current)
        
        for i in range(len(restrictions)-1,0,-1):
            distance=restrictions[i][0]-restrictions[i-1][0]
            current=restrictions[i][1]+distance
            restrictions[i-1][1]=min(restrictions[i-1][1],current)
        
        for i in range(len(restrictions)-1):
            max_height=max(max_height,(restrictions[i+1][0]-restrictions[i][0]+restrictions[i][1]+restrictions[i+1][1])//2)
        return max_height