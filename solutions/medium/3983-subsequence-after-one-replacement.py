# ─────────────────────────────────────────────────
#  Problem : 3983. Subsequence After One Replacement
#  Difficulty : Medium
#  Runtime  : 0 ms
#  Memory   : 12.4 MB
#  Solved   : 2026-08-08
# ─────────────────────────────────────────────────

class Solution(object):
    def canMakeSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        n=len(s)
        i=0
        j=0
        while i<len(s) and j<len(t):
            if s[i]==t[j]:
                n-=1
                i+=1
            j+=1
        if i==len(s) or n==1:
            return True
        return False