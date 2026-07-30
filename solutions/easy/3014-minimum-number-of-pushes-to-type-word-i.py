# ─────────────────────────────────────────────────
#  Problem : 3014. Minimum Number of Pushes to Type Word I
#  Difficulty : Easy
#  Runtime  : 0 ms
#  Memory   : 12.3 MB
#  Solved   : 2026-07-30
# ─────────────────────────────────────────────────

class Solution(object):
    def minimumPushes(self, word):
        """
        :type word: str
        :rtype: int
        """
        n=len(word)
        div=n/8
        ans=0
        for i in range(1,div+1):
            ans+=i*8
        n-=(div*8)
        ans+=n*(div+1)
        return ans