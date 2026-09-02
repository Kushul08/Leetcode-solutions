# ─────────────────────────────────────────────────
#  Problem : 0073. Set Matrix Zeroes
#  Difficulty : Medium
#  Runtime  : 289 ms
#  Memory   : 14.6 MB
#  Solved   : 2026-09-02
# ─────────────────────────────────────────────────

class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        # length=len(matrix[0])
        # for num in matrix:
        #     if 0 in num:
        #         num=[0]*length
        # return matrix
        indices=[]
        zeroes=False
        for num in matrix:
            zeroes=False
            for i in range(len(num)):
                if num[i]==0:
                    zeroes=True
                    indices.append(i)
            if zeroes:
                for i in range(len(num)):
                    num[i]=0
        for num in matrix:
            for i in range(len(indices)):
                num[indices[i]]=0
        return matrix