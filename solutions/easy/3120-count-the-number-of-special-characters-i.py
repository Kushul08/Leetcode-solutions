# ─────────────────────────────────────────────────
#  Problem : 3120. Count the Number of Special Characters I
#  Difficulty : Easy
#  Runtime  : 0 ms
#  Memory   : 12.5 MB
#  Solved   : 2026-05-26
# ─────────────────────────────────────────────────

class Solution(object):
    def numberOfSpecialChars(self, word):
        """
        :type word: str
        :rtype: int
        """
        seen=set(word)
        count=0
        for w in seen: 
            if chr(ord(w)-32) in seen:
                count+=1
        return count