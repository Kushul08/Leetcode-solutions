# ─────────────────────────────────────────────────
#  Problem : 3483. Unique 3-Digit Even Numbers
#  Difficulty : Easy
#  Runtime  : 23 ms
#  Memory   : 12.5 MB
#  Solved   : 2026-09-11
# ─────────────────────────────────────────────────

class Solution(object):
    def totalNumbers(self, digits):
        """
        :type digits: List[int]
        :rtype: int
        """
        n=len(digits)
        seen=set()
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    if i!=j and j!=k and i!=k and digits[k]%2==0 and digits[i]!=0:
                        seen.add((digits[i],digits[j],digits[k]))
        return len(seen)