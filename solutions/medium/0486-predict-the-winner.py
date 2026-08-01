# ─────────────────────────────────────────────────
#  Problem : 0486. Predict the Winner
#  Difficulty : Medium
#  Runtime  : 2056 ms
#  Memory   : 19.3 MB
#  Solved   : 2026-08-01
# ─────────────────────────────────────────────────

class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        n=len(nums)
        def recur(x,y,diff,flag):
            if y==x:
                if flag: 
                    diff+=nums[x]
                else:
                    diff-=nums[x]
                return diff
            if flag:
                return max(recur(x+1,y,diff+nums[x],False),
                recur(x,y-1,diff+nums[y],False))
            else:
                return  min(recur(x+1,y,diff-nums[x],True),
                recur(x,y-1,diff-nums[y],True)) # he wants the difference as small as possible
        return recur(0,n-1,0,True)>=0       