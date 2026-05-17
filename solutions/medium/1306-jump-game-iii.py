# ─────────────────────────────────────────────────
#  Problem : 1306. Jump Game III
#  Difficulty : Medium
#  Runtime  : 29 ms
#  Memory   : 16.2 MB
#  Solved   : 2026-05-17
# ─────────────────────────────────────────────────

from collections import deque
class Solution(object):
    def canReach(self, arr, start):
        """
        :type arr: List[int]
        :type start: int
        :rtype: bool
        """
        queue=deque([start])
        dp=[False]*(len(arr))
        dp[start]=True
        zeros=set()
        for i in range(len(arr)):
            if arr[i]==0:
                zeros.add(i)
        if start in zeros:
            return True
        while queue:
            # if dp[target]==True:
            #     return True
            i=queue.popleft()
            left=i-arr[i]
            right=i+arr[i]
            if 0<=left and dp[left]==False:
                queue.append(left)
                dp[left]=True
            if right<len(arr) and dp[right]==False:
                queue.append(right)
                dp[right]=True
            if left in zeros or right in zeros: return True
        return False