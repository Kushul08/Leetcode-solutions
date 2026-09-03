# ─────────────────────────────────────────────────
#  Problem : 1901. Find a Peak Element II
#  Difficulty : Medium
#  Runtime  : 0 ms
#  Memory   : 12.4 MB
#  Solved   : 2026-09-03
# ─────────────────────────────────────────────────

class Solution(object):
    def findPeakGrid(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        low=0
        high=len(mat[0])-1

        while low<=high:

            col=(low+high)>>1

            max_row=0

            for row in range(len(mat)):
                if mat[row][col]>mat[max_row][col]:
                    max_row=row
            
            left_val=mat[max_row][col-1] if col-1>=0 else -1
            
            right_val=mat[max_row][col+1] if col+1<len(mat[0]) else -1

            peak=mat[max_row][col]

            if peak>left_val and peak>right_val:
                return [max_row,col]
            elif peak>left_val and peak<right_val:
                low=col+1
            else:
                high=mid-1