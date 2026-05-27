# ─────────────────────────────────────────────────
#  Problem : 3121. Count the Number of Special Characters II
#  Difficulty : Medium
#  Runtime  : 72 ms
#  Memory   : 14.7 MB
#  Solved   : 2026-05-27
# ─────────────────────────────────────────────────

class Solution(object):
    def numberOfSpecialChars(self, word):
        """
        :type word: str
        :rtype: int
        """
        count=0
        for i in range(ord('a'),ord('z')+1):
            lower=chr(i)
            cap=chr(i-32)

            if lower in word and cap in word:
                if word.rindex(lower)<word.index(cap):
                    count+=1
        return count