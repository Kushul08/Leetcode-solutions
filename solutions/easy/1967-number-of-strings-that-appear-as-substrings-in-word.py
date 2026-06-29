# ─────────────────────────────────────────────────
#  Problem : 1967. Number of Strings That Appear as Substrings in Word
#  Difficulty : Easy
#  Runtime  : 19 ms
#  Memory   : 12.8 MB
#  Solved   : 2026-06-29
# ─────────────────────────────────────────────────

class Solution(object):
    def numOfStrings(self, patterns, word):
        """
        :type patterns: List[str]
        :type word: str
        :rtype: int
        """
        sub_string=set()
        for i in range(len(word)):
            string=''
            for j in range(i,len(word)):
                string+=word[j]
                sub_string.add(string)
        count=0
        for pattern in patterns:
            if pattern in sub_string:
                count+=1
        return count