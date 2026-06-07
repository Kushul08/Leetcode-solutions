# ─────────────────────────────────────────────────
#  Problem : 3955. Valid Binary Strings With Cost Limit
#  Difficulty : Medium
#  Runtime  : 60 ms
#  Memory   : 14.1 MB
#  Solved   : 2026-06-07
# ─────────────────────────────────────────────────

class Solution(object):
    def generateValidStrings(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[str]
        """
        ans=[]
        def helper(string,cost):
            if cost>k:
                return
            if len(string)==n:
                ans.append(string)
                return
            if len(string)==0:
                helper(string+'0',cost)
                helper(string+'1',cost)
            else:
                if string[-1]=='0':
                    helper(string+'0',cost)
                    helper(string+'1',cost+len(string))
                else:
                    helper(string+'0',cost)
        helper('',0)
        return ans