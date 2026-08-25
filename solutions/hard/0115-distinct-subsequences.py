# ─────────────────────────────────────────────────
#  Problem : 0115. Distinct Subsequences
#  Difficulty : Hard
#  Runtime  : 0 ms
#  Memory   : 19.2 MB
#  Solved   : 2026-08-25
# ─────────────────────────────────────────────────

class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        n=len(s)
        def recur(i,string):
            if i==n:
                return 1 if string==t else 0
            if string and string[0]!=t[0]:
                return 0
            return recur(i+1,string+s[i])+recur(i+1,string)

        return (recur(0,''))