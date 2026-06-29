# ─────────────────────────────────────────────────
#  Problem : 1967. Number of Strings That Appear as Substrings in Word
#  Difficulty : Easy
#  Runtime  : 0 ms
#  Memory   : 12.5 MB
#  Solved   : 2026-06-29
# ─────────────────────────────────────────────────

class Solution(object):
    def numOfStrings(self, patterns, word):
        """
        :type patterns: List[str]
        :type word: str
        :rtype: int
        """
        count=0
        for pattern in patterns:
            if pattern in word:
                count+=1
        return count