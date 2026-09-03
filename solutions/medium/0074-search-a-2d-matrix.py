# ─────────────────────────────────────────────────
#  Problem : 0074. Search a 2D Matrix
#  Difficulty : Medium
#  Runtime  : 0 ms
#  Memory   : 12.5 MB
#  Solved   : 2026-09-03
# ─────────────────────────────────────────────────

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        
        low,high=0,len(matrix)-1
        row=-1

        while low<=high:
            mid=(low+high)//2
            if matrix[mid][0]<=target:
                row=mid
                low=mid+1
            else:
                high=mid-1
        
        find=-1
        low,high=0,len(matrix[row])-1

        while low<=high:
            mid=(low+high)//2
            if matrix[row][mid]<=target:
                find=matrix[row][mid]
                low=mid+1
            else:
                high=mid-1
            
        return find==target