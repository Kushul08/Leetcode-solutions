# ─────────────────────────────────────────────────
#  Problem : 1143. Longest Common Subsequence
#  Difficulty : Medium
#  Runtime  : 601 ms
#  Memory   : 44.3 MB
#  Solved   : 2026-08-17
# ─────────────────────────────────────────────────

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        n,m=len(text1),len(text2)

        dp=[[-1]*m for _ in range(n)]
        def recur(i,j):
            if i<0 or j<0: return 0
            if dp[i][j]!=-1:
                return dp[i][j]
            if text1[i]==text2[j]:
                return recur(i-1,j-1)+1
            else:
                dp[i][j]=max(recur(i-1,j),recur(i,j-1))
                return dp[i][j]
        return recur(n-1,m-1)
