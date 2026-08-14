# ─────────────────────────────────────────────────
#  Problem : 3090. Maximum Length Substring With Two Occurrences
#  Difficulty : Easy
#  Runtime  : 3 ms
#  Memory   : 12.5 MB
#  Solved   : 2026-08-14
# ─────────────────────────────────────────────────

class Solution(object):
    def maximumLengthSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        hashmap={}
        l=0
        r=0
        max_len=0
        while r<len(s):
            hashmap[s[r]]=hashmap.get(s[r],0)+1
            while hashmap[s[r]]>2:
                hashmap[s[l]]-=1
                l+=1
            max_len=max(max_len,r-l+1)
            r+=1
        return max_len