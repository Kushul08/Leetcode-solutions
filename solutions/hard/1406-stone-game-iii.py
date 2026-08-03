# ─────────────────────────────────────────────────
#  Problem : 1406. Stone Game III
#  Difficulty : Hard
#  Runtime  : 0 ms
#  Memory   : 19.4 MB
#  Solved   : 2026-08-03
# ─────────────────────────────────────────────────

class Solution(object):
    def stoneGameIII(self, stoneValue):
        """
        :type stoneValue: List[int]
        :rtype: str
        """
        n=len(stoneValue)
        alice=0
        bob=0
        i=0
        flag=True
        while i<n:
            points=stoneValue[i]
            step=1
            if i+1<n:
                if points<=stoneValue[i+1]:
                    points+=stoneValue[i+1]
                    step=2
            if i+2<n:
                if points<=stoneValue[i+2]:
                    points+=stoneValue[i+2]
                    step=3
            if flag==True:
                alice+=points
                flag=False
            else:
                bob+=points
                flag=True
            i+=step
        if alice==bob:
            return 'Tie'
        elif alice<bob:
            return 'Bob'
        else:
            return 'Alice'