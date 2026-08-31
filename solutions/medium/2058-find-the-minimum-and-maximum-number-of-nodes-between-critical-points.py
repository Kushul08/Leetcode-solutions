# ─────────────────────────────────────────────────
#  Problem : 2058. Find the Minimum and Maximum Number of Nodes Between Critical Points
#  Difficulty : Medium
#  Runtime  : 295 ms
#  Memory   : 90.4 MB
#  Solved   : 2026-08-31
# ─────────────────────────────────────────────────

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def nodesBetweenCriticalPoints(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: List[int]
        """
        curr=head
        prev=None
        first=None
        prev_local=None
        ans=[1e9,-1]
        indx=1
        while curr:
            if not curr.next:
                break
            next=curr.next
            if prev and prev.val<curr.val and curr.val>next.val:
                if first==None:
                    first=indx
                    prev_local=indx
                else:
                    ans[0]=min(indx-prev_local,ans[0])
                    ans[1]=max(indx-first,ans[1])
                    prev_local=indx
            if prev and prev.val>curr.val and curr.val<next.val:
                if first==None:
                    first=indx
                    prev_local=indx
                else:
                    ans[0]=min(indx-prev_local,ans[0])
                    ans[1]=max(indx-first,ans[1])
                    prev_local=indx
            indx+=1
            prev=curr
            curr=curr.next
        return ans if ans[0]!=1e9 else [-1,-1]
            