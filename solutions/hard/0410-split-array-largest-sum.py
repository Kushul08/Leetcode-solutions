# ─────────────────────────────────────────────────
#  Problem : 0410. Split Array Largest Sum
#  Difficulty : Hard
#  Runtime  : 3 ms
#  Memory   : 19.4 MB
#  Solved   : 2026-09-03
# ─────────────────────────────────────────────────

class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        

        def help(val):
            sums=0
            count=0
            for num in nums:
                if num+sums<=val:
                    sums+=num
                else:
                    count+=1
                    sums=num
            return count
        
        low=max(nums)
        high=sum(nums)

        while low<=high:
            mid=(low+high)>>1

            if help(mid)>=k:
                low=mid+1
            else:
                high=mid-1
        return low