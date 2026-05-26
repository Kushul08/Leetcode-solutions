# ─────────────────────────────────────────────────
#  Problem : 3120. Count the Number of Special Characters I
#  Difficulty : Easy
#  Runtime  : 0 ms
#  Memory   : 12.3 MB
#  Solved   : 2026-05-26
# ─────────────────────────────────────────────────

class Solution(object):
    def numberOfSpecialChars(self, word):
        """
        :type word: str
        :rtype: int
        """
        set_word=set(word)
        count=0
        for char in set_word: 
            if char.isupper() and char.lower() in set_word:
                count+=1
        return count