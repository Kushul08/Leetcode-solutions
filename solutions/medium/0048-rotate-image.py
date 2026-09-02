# ─────────────────────────────────────────────────
#  Problem : 0048. Rotate Image
#  Difficulty : Medium
#  Runtime  : 7 ms
#  Memory   : 12.2 MB
#  Solved   : 2026-09-02
# ─────────────────────────────────────────────────

class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n=len(matrix)
        for i in range(n):
            for j in range(i+1,n):
                print(matrix[i][j],matrix[j][i])
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        for num in matrix:
            for i in range(len(num)//2):
                num[i],num[n-i-1]=num[n-i-1],num[i]