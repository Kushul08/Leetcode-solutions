# ─────────────────────────────────────────────────
#  Problem : 4011. Count Subarrays With Even Odd Ratio I
#  Difficulty : Medium
#  Runtime  : 1626 ms
#  Memory   : 19.3 MB
#  Solved   : 2026-08-02
# ─────────────────────────────────────────────────

class Solution:
    def countRatioSubarrays(self, nums: list[int], a: int, b: int) -> int:
        val=a/b
        count=0
        for i in range(len(nums)):
            even=odd=0
            if nums[i]%2==0:
                even+=1
            else:
                odd+=1
            if odd>0:
                count+=1
            for j in range(i+1,len(nums)):
                if nums[j]%2==0:
                    even+=1
                else:
                    odd+=1
                if odd>0:
                    # print(i,j)
                    if (even/odd)<=val:
                        count+=1
        return count