# ─────────────────────────────────────────────────
#  Problem : 1189. Maximum Number of Balloons
#  Difficulty : Easy
#  Runtime  : 7 ms
#  Memory   : 12.4 MB
#  Solved   : 2026-06-22
# ─────────────────────────────────────────────────

from collections import Counter
class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        text_freq=Counter(text)
        ballon_freq=Counter('balloon')

        instances=float('inf')
        for char in 'ballon':
            instances=min(instances,text_freq[char]/ballon_freq[char])
        if instances==float('inf'):
            return 0
        return instances