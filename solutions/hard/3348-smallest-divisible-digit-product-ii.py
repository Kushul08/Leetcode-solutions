# ─────────────────────────────────────────────────
#  Problem : 3348. Smallest Divisible Digit Product II
#  Difficulty : Hard
#  Runtime  : 0 ms
#  Memory   : 19.1 MB
#  Solved   : 2026-08-07
# ─────────────────────────────────────────────────

class Solution(object):
    def smallestNumber(self, num, t):
        """
        :type num: str
        :type t: int
        :rtype: str
        """
        def find_prod(val):
            ans=1
            while val:
                ans*=val%10
                val=val//10
            return ans
        number=int(num)
        for i in range(number,pow(10,6)):
            if i%10==0: continue
            product=find_prod(i)
            if product==0: continue
            if product>=t and product%t==0:
                return str(i)
        return '-1'