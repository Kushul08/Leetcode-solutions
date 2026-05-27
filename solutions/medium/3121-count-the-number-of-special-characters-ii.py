# ─────────────────────────────────────────────────
#  Problem : 3121. Count the Number of Special Characters II
#  Difficulty : Medium
#  Runtime  : 265 ms
#  Memory   : 20.8 MB
#  Solved   : 2026-05-27
# ─────────────────────────────────────────────────

class Solution(object):
    def numberOfSpecialChars(self, word):
        """
        :type word: str
        :rtype: int
        """
        caps={}
        lower={}
        seen=set()
        for i in range(len(word)):
            char=word[i]
            if char.isupper():
                if char not in caps:
                    caps[char]=i
            else:
                lower[char]=i
            
        count=0
        for key,val in caps.items():
            if key.lower() in lower:
                if lower[key.lower()]<val:
                    count+=1
        return count