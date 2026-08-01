# ─────────────────────────────────────────────────
#  Problem : 0486. Predict the Winner
#  Difficulty : Medium
#  Runtime  : 0 ms
#  Memory   : 20.2 MB
#  Solved   : 2026-08-01
# ─────────────────────────────────────────────────

from functools import lru_cache
class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        n=len(nums)

        @lru_cache(None)
        def recur(x,y,turn):
            if y==x:
                if turn: 
                    return nums[x]
                else:
                    return -nums[x]
            if turn:
                return max(nums[x]+recur(x+1,y,False),
                nums[y]+recur(x,y-1,False))
            else:
                return  min(recur(x+1,y,True)-nums[x],
                recur(x,y-1,True)-nums[y]) # he wants the difference as small as possible
        return recur(0,n-1,True)>=0       