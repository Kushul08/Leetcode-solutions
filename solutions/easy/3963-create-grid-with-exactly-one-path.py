# ─────────────────────────────────────────────────
#  Problem : 3963. Create Grid With Exactly One Path
#  Difficulty : Easy
#  Runtime  : 8 ms
#  Memory   : 12.4 MB
#  Solved   : 2026-06-21
# ─────────────────────────────────────────────────

class Solution(object):
    def createGrid(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: List[str]
        """
        grid=[['#' for _ in range(n)] for _ in range(m)]
        for  i in range(len(grid)):
            grid[i][0]='.'
        for i in range(len(grid[0])):
            grid[-1][i]='.'
        ans=[]
        for row in grid:
            ans.append(''.join(row))
        return ans