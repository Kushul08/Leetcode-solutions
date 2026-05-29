# ─────────────────────────────────────────────────
#  Problem : 1056. Confusing Number
#  Difficulty : Easy
#  Runtime  : 0 ms
#  Memory   : 12.5 MB
#  Solved   : 2026-05-29
# ─────────────────────────────────────────────────

class Solution(object):
    def confusingNumber(self, n):
        """
        :type n: int
        :rtype: bool
        """
        rotated ={0:0,1:1,6:9,8:8,9:6}
        ans=0
        num=n
        while num>0:
            val=num%10
            if val in rotated:
                ans=ans*10+rotated[val]
            else:
                return False
            num=num//10
        return ans!=n