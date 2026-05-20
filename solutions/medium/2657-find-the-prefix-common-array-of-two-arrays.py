# ─────────────────────────────────────────────────
#  Problem : 2657. Find the Prefix Common Array of Two Arrays
#  Difficulty : Medium
#  Runtime  : 2 ms
#  Memory   : 12.5 MB
#  Solved   : 2026-05-20
# ─────────────────────────────────────────────────

class Solution(object):
    def findThePrefixCommonArray(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        common=set()
        ans=[]
        for i in range(len(A)):
            common.add(A[i])
            common.add(B[i])
            total=i*2+2
            ans.append(total-len(common))
        return ans