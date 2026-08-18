# ─────────────────────────────────────────────────
#  Problem : 0516. Longest Palindromic Subsequence
#  Difficulty : Medium
#  Runtime  : 0 ms
#  Memory   : 19.2 MB
#  Solved   : 2026-08-18
# ─────────────────────────────────────────────────

class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        n=len(s)
        s1=s
        s2=s[::-1]

        def recur(i,j):
            if i<0 or j<0:
                return 0
            if s1[i]==s2[j]:
                return recur(i-1,j-1)+1
            else:
                return max(recur(i,j-1),recur(i-1,j))
        return recur(n-1,n-1)