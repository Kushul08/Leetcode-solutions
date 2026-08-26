# ─────────────────────────────────────────────────
#  Problem : 0044. Wildcard Matching
#  Difficulty : Hard
#  Runtime  : 0 ms
#  Memory   : 12.3 MB
#  Solved   : 2026-08-26
# ─────────────────────────────────────────────────

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        n,m=len(s),len(p)
        def recur(i,j):
            if i<0 or j<0:
                if i<0:
                    return True
                return False 
            if s[i]==p[j]:
                return recur(i-1,j-1)
            elif p[j]=='*':
                return recur(i-1,j-1) or recur(i-1,j)
            elif p[j]=='?':
                return recur(i-1,j-1)
            else:
                return False
        return recur(n-1,m-1)