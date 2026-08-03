# ─────────────────────────────────────────────────
#  Problem : 1406. Stone Game III
#  Difficulty : Hard
#  Runtime  : 0 ms
#  Memory   : 19.4 MB
#  Solved   : 2026-08-03
# ─────────────────────────────────────────────────

class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        
        n=len(stoneValue)
        def recur(i,diff,turn):
            if i>=n:
                return diff
            if turn:
                one=recur(i+1,diff+stoneValue[i],False)
                two=recur(i+2,diff+stoneValue[i]+stoneValue[i+1],False) if i+1<n else float('-inf')
                three=recur(i+3,diff+stoneValue[i]+stoneValue[i+1]+stoneValue[i+2],False) if i+2<n else float('-inf')
                return max(one,two,three)
            else:
                one=recur(i+1,diff-stoneValue[i],True)
                two=recur(i+2,diff-stoneValue[i]-stoneValue[i+1],True) if i+1<n else float('inf')
                three=recur(i+3,diff-stoneValue[i]-stoneValue[i+1]-stoneValue[i+2],True) if i+2<n else float('inf')
                return min(one,two,three)
        value=recur(0,0,True)
        if value<0:
            return 'Bob'
        elif value==0:
            return 'Tie'
        else:
            return 'Alice'