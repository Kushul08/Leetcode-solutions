# ─────────────────────────────────────────────────
#  Problem : 1477. Find Two Non-overlapping Sub-arrays Each With Target Sum
#  Difficulty : Medium
#  Runtime  : 308 ms
#  Memory   : 32.9 MB
#  Solved   : 2026-09-17
# ─────────────────────────────────────────────────

class Solution(object):
    def minSumOfLengths(self, arr, target):
        """
        :type arr: List[int]
        :type target: int
        :rtype: int
        """
        n=len(arr)
        hashmap={0:-1}
        sums=0
        dp=[(1e9)]*n
        min_so_far=1e9
        min_total_len=1e9
        for i,num in enumerate(arr):
            sums+=num
            if i>0:
                min_so_far=min(min_so_far,dp[i-1])
            if sums-target in hashmap:
                start=hashmap[sums-target]
                curr_len=i-start

                dp[i]=min(min_so_far,curr_len)

                if start>=0 and dp[start]!=1e9:
                    min_total_len=min(min_total_len,curr_len+dp[start])
            else:
                dp[i]=min_so_far
            hashmap[sums]=i
        return min_total_len if min_total_len!=1e9 else -1