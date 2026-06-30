# ─────────────────────────────────────────────────
#  Problem : 1358. Number of Substrings Containing All Three Characters
#  Difficulty : Medium
#  Runtime  : 97 ms
#  Memory   : 12.4 MB
#  Solved   : 2026-06-30
# ─────────────────────────────────────────────────

class Solution(object):
    def numberOfSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Bruteforce is to generate all substring which takes a time complexity of O(n^2), but constraints not allow this
        chars={}
        count=0
        for i,ch in enumerate(s):
            chars[ch]=i
            if len(chars)==3:
                count+=min(chars.values())+1
        return count