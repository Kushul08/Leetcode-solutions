# ─────────────────────────────────────────────────
#  Problem : 3483. Unique 3-Digit Even Numbers
#  Difficulty : Easy
#  Runtime  : 16 ms
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
        seen=[False]*1000
        ans=0
        for i in range(n):
            if digits[i]==0: continue
            for j in range(n):
                if i==j: continue
                for k in range(n):
                    if k==j or k==i or digits[k]%2==1: continue
                    val=digits[i]*100+digits[j]*10+digits[k]
                    if seen[val]==False:
                        seen[val]=True
                        ans+=1
        return ans