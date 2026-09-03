# ─────────────────────────────────────────────────
#  Problem : 0240. Search a 2D Matrix II
#  Difficulty : Medium
#  Runtime  : 127 ms
#  Memory   : 18.5 MB
#  Solved   : 2026-09-03
# ─────────────────────────────────────────────────

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        row=0
        col=len(matrix[0])-1

        while row<len(matrix) and col>=0:
            if matrix[row][col]==target:
                return True
            elif matrix[row][col]<target:
                row+=1
            else:
                col-=1
        return False
            