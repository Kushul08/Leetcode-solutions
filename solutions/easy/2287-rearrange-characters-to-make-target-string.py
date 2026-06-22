# ─────────────────────────────────────────────────
#  Problem : 2287. Rearrange Characters to Make Target String
#  Difficulty : Easy
#  Runtime  : 0 ms
#  Memory   : 12.3 MB
#  Solved   : 2026-06-22
# ─────────────────────────────────────────────────

from collections import Counter
class Solution(object):
    def rearrangeCharacters(self, s, target):
        """
        :type s: str
        :type target: str
        :rtype: int
        """
        hashmap=Counter(s)
        freq=Counter(target)
        copies=float('inf')
        for char in target:
            copies=min(copies,hashmap[char]/freq[char])
        if copies==float('inf'): return 0
        return copies