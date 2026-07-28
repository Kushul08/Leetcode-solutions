# ─────────────────────────────────────────────────
#  Problem : 3517. Smallest Palindromic Rearrangement I
#  Difficulty : Medium
#  Runtime  : 284 ms
#  Memory   : 13.4 MB
#  Solved   : 2026-07-28
# ─────────────────────────────────────────────────

class Solution(object):
    def smallestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        counter=defaultdict(int)
        for ch in s:
            counter[ch]+=1
        double=''
        single=''
        for ch in string.ascii_lowercase:
            double+=ch*(counter[ch]/2)
            if counter[ch]%2!=0:
                single+=ch
        return double+single+double[::-1]