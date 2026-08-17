# ─────────────────────────────────────────────────
#  Problem : 1563. Stone Game V
#  Difficulty : Hard
#  Runtime  : 0 ms
#  Memory   : 19.3 MB
#  Solved   : 2026-08-17
# ─────────────────────────────────────────────────

class Solution(object):
    def stoneGameV(self, stoneValue):
        """
        :type stoneValue: List[int]
        :rtype: int
        """
        
        def recur(l,r):
            if r-l+1<2:
                return 0
            ans=0
            for k in range(l,r+1):
                left_sum=sum(stoneValue[l:k+1])
                right_sum=sum(stoneValue[k+1:r+1])

                if left_sum<right_sum:
                    curr=recur(l,k)+left_sum
                elif right_sum<left_sum:
                    curr=recur(k+1,r)+right_sum
                else:
                    curr=left_sum+max(recur(l,k),recur(k+1,r))
                ans=max(ans,curr)
            return ans
        return recur(0,len(stoneValue)-1)