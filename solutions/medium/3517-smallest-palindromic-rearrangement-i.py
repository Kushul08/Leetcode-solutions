# ─────────────────────────────────────────────────
#  Problem : 3517. Smallest Palindromic Rearrangement I
#  Difficulty : Medium
#  Runtime  : 796 ms
#  Memory   : 13.7 MB
#  Solved   : 2026-07-28
# ─────────────────────────────────────────────────

from collections import Counter
class Solution(object):
    def smallestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        counter=Counter(s)
        left=middle=right=''
        new_s=sorted(set(s))
        for ch in new_s:
            left+=ch*(counter[ch]/2)
            if counter[ch]%2!=0:
                middle+=ch
            right+=ch*(counter[ch]/2)
        return left+middle+right[::-1]