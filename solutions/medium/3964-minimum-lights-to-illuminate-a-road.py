# ─────────────────────────────────────────────────
#  Problem : 3964. Minimum Lights to Illuminate a Road
#  Difficulty : Medium
#  Runtime  : 524 ms
#  Memory   : 35.4 MB
#  Solved   : 2026-07-04
# ─────────────────────────────────────────────────

import math
class Solution:
    def minLights(self, lights: list[int]) -> int:
        n=len(lights)
        nums=set(i for i in range(len(lights)))
        for i in range(len(lights)):
            # print('hello',lights[i])
            if lights[i]!=0:
                start=max(0,i-lights[i])
                end=min(n-1,i+lights[i])
                if start  not in nums and end not in nums: continue
                for val in range(start,end+1):
                    if val in nums:
                        nums.remove(val)
        sequence=[]
        count=0
        nums=list(nums)
        if not nums: return 0
        nums.append(int(1e9))
        if len(nums)==1: return 1
        for i in range(1,len(nums)):
            if nums[i-1]+1==nums[i]:
                count+=1
            else:
                sequence.append(count+1)
                count=0
        # print(sequence)
        min_lights=0
        # print(sequence)
        for num in sequence:
            if num<=2:
                min_lights+=1
            else:
                min_lights+=(math.ceil(num/3))
        return min_lights