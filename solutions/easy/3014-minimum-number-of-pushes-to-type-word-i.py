# ─────────────────────────────────────────────────
#  Problem : 3014. Minimum Number of Pushes to Type Word I
#  Difficulty : Easy
#  Runtime  : 0 ms
#  Memory   : 12.2 MB
#  Solved   : 2026-07-30
# ─────────────────────────────────────────────────

class Solution(object):
    def minimumPushes(self, word):
        """
        :type word: str
        :rtype: int
        """
        ans=0
        count=0
        for _ in range(len(word)):
            count+=1
            if count<=8:
                ans+=1
            elif count<=16:
                ans+=2
            elif count<=24:
                ans+=3
            else:
                ans+=4
        return ans