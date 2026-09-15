# ─────────────────────────────────────────────────
#  Problem : 1762. Buildings With an Ocean View
#  Difficulty : Medium
#  Runtime  : 54 ms
#  Memory   : 28.3 MB
#  Solved   : 2026-09-15
# ─────────────────────────────────────────────────

class Solution(object):
    def findBuildings(self, heights):
        """
        :type heights: List[int]
        :rtype: List[int]
        """
        ans=[]
        max_val=-1
        for i in range(len(heights)-1,-1,-1):
            if heights[i]>max_val:
                ans.append(i)
            max_val=max(max_val,heights[i])
        return ans[::-1]