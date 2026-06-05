# ─────────────────────────────────────────────────
#  Problem : 3753. Total Waviness of Numbers in Range II
#  Difficulty : Hard
#  Runtime  : 724 ms
#  Memory   : 20.8 MB
#  Solved   : 2026-06-05
# ─────────────────────────────────────────────────

from functools import lru_cache
def solve(N):
    digit=list(map(int,str(N)))
    n=len(digit)
    @lru_cache(maxsize=None)
    def count(pos,tight):
        if pos==n:
            return 1
        limit=digit[pos] if tight else 9
        result=0
        for d in range(limit+1):
            result+=count(pos+1,tight and d==limit)
        return result
    @lru_cache(maxsize=None)
    def dp(pos,tight,prev,prev_prev,started):
        if pos==n:
            return 0
        result=0
        limit=digit[pos] if tight else 9
        for d in range(limit+1):
            new_tight=tight and (d==limit)
            if not started and d==0:
                result+=dp(pos+1,new_tight,-1,-1,False)
            else:
                contribution=0
                if prev!=-1 and prev_prev!=-1:
                    if (prev_prev<prev>d) or (prev_prev>prev<d):
                        contribution+=count(pos+1,new_tight)
                result+=contribution+dp(pos+1,new_tight,d,prev,True)
        return result
    ans=dp(0,True,-1,-1,False)
    dp.cache_clear()
    count.cache_clear()
    return ans
class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        return solve(num2)-solve(num1-1)