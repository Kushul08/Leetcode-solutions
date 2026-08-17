# ─────────────────────────────────────────────────
#  Problem : 1143. Longest Common Subsequence
#  Difficulty : Medium
#  Runtime  : 0 ms
#  Memory   : 19.3 MB
#  Solved   : 2026-08-17
# ─────────────────────────────────────────────────

class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        n,m=len(text1),len(text2)
        def recur(i,j):
            if i<0 or j<0: return 0
            if text1[i]==text2[j]:
                return recur(i-1,j-1)+1
            else:
                return max(recur(i-1,j),recur(i,j-1))
        return recur(n-1,m-1)