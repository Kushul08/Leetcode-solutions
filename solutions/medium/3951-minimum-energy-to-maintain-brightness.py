# ─────────────────────────────────────────────────
#  Problem : 3951. Minimum Energy to Maintain Brightness
#  Difficulty : Medium
#  Runtime  : 83 ms
#  Memory   : 57.5 MB
#  Solved   : 2026-06-07
# ─────────────────────────────────────────────────

class Solution:
    def minEnergy(self, n: int, brightness: int, intervals: list[list[int]]) -> int:
        bulbs=(brightness//3)+1 if brightness/3>brightness//3 else brightness//3
        intervals.sort()
        stack=[]
        for interval in intervals:
            if not stack:
                stack.append(interval)
                continue
            if stack[-1][1]>=interval[0]:
                stack[-1][1]=max(stack[-1][1],interval[1])
            else:
                stack.append(interval)
        ans=0
        for interval in stack:
            ans+=(interval[1]-interval[0]+1)
        return ans*bulbs