# ─────────────────────────────────────────────────
#  Problem : 4006. Count Valid Prefixes
#  Difficulty : Easy
#  Runtime  : 3 ms
#  Memory   : 12.4 MB
#  Solved   : 2026-08-07
# ─────────────────────────────────────────────────

class Solution(object):
    def countValidPrefixes(self, s):
        """
        :type s: str
        :rtype: int
        """
        ones=0
        zeros=0
        ans=0
        for num in s:
            if num=='1': ones+=1
            else: zeros+=1
            if abs(ones-zeros)<=1:
                ans+=1
        return ans