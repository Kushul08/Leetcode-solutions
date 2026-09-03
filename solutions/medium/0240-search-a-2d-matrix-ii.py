# ─────────────────────────────────────────────────
#  Problem : 0240. Search a 2D Matrix II
#  Difficulty : Medium
#  Runtime  : 15 ms
#  Memory   : 12.2 MB
#  Solved   : 2026-09-03
# ─────────────────────────────────────────────────

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        n,m=len(matrix),len(matrix[0])
        low=0
        high=m-1

        while low<=high:
            mid=(low+high)>>1
            print(low,high,mid)

            if matrix[0][mid]==target:
                return True
            elif matrix[0][mid]>target:
                high=mid-1
            else:
                low=mid+1
        col=high
        low=0
        high=n-1

        while low<=high:
            mid=(low+high)>>1

            if matrix[mid][col]==target:
                return True
            elif matrix[mid][col]>target:
                high=mid-1
            else:
                low=mid+1
        return False