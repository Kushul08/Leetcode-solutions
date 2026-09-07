# ─────────────────────────────────────────────────
#  Problem : 0940. Distinct Subsequences II
#  Difficulty : Hard
#  Runtime  : 0 ms
#  Memory   : 19.4 MB
#  Solved   : 2026-09-07
# ─────────────────────────────────────────────────

class Solution(object):
    def distinctSubseqII(self, s):
        """
        :type s: str
        :rtype: int
        """
        n=len(s)
        hashset=set()
        MOD=int(1e9+7)
        def recur(i,string):
            if i==n:
                hashset.add(string)
                return
            recur(i+1,string)
            recur(i+1,string+s[i])
        recur(0,'')
        return (len(hashset)-1)%MOD