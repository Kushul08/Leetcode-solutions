# ─────────────────────────────────────────────────
#  Problem : 3614. Process String with Special Operations II
#  Difficulty : Hard
#  Runtime  : 515 ms
#  Memory   : 12.7 MB
#  Solved   : 2026-06-17
# ─────────────────────────────────────────────────

class Solution(object):
    def processStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        length=0
        for char in s:
            if char=='*':
                length=max(0,length-1)
            elif char=='#':
                length*=2
            elif char=='%':
                pass
            else:
                length+=1
        if length==0 or k>=length:
            return '.'

        for char in reversed(s):
            if char.isalpha():
                if k==length-1:
                    return char
                length-=1
            elif char=='#':
                length//=2
                k%=length
            elif char=='*':
                length+=1
            else:
                k=length-k-1
        return '.'