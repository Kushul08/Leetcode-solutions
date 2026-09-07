# ─────────────────────────────────────────────────
#  Problem : 0940. Distinct Subsequences II
#  Difficulty : Hard
#  Runtime  : 14 ms
#  Memory   : 12.5 MB
#  Solved   : 2026-09-07
# ─────────────────────────────────────────────────

class Solution(object):
    def distinctSubseqII(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp=[1]
        MOD=int(1e9+7)
        seen={}
        for i,ch in enumerate(s):
            dp.append((dp[-1]*2)%MOD)
            if ch in seen:
                dp[-1]-=dp[seen[ch]]
            seen[ch]=i
        return (dp[-1]-1)%MOD