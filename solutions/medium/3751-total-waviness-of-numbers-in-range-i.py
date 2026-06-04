# ─────────────────────────────────────────────────
#  Problem : 3751. Total Waviness of Numbers in Range I
#  Difficulty : Medium
#  Runtime  : 389 ms
#  Memory   : 15.2 MB
#  Solved   : 2026-06-04
# ─────────────────────────────────────────────────

class Solution(object):
    def totalWaviness(self, num1, num2):
        """
        :type num1: int
        :type num2: int
        :rtype: int
        """
        wavi=0
        num1=max(100,num1)
        for num in range(num1,num2+1):
            val=str(num)
            for i in range(1,len(val)-1):
                if (val[i-1]<val[i] and val[i]>val[i+1]) or (val[i-1]>val[i] and val[i]<val[i+1]):
                    wavi+=1
        return wavi