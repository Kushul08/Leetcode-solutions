# ─────────────────────────────────────────────────
#  Problem : 2130. Maximum Twin Sum of a Linked List
#  Difficulty : Medium
#  Runtime  : 232 ms
#  Memory   : 71.3 MB
#  Solved   : 2026-06-14
# ─────────────────────────────────────────────────

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        curr=head
        slow=head
        fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        prev=None
        while slow:
            nxt=slow.next
            slow.next=prev
            prev=slow
            slow=nxt
        
        left=head
        right=prev
        max_sum=0
        while left and right:
            max_sum=max(max_sum,left.val+right.val)
            left=left.next
            right=right.next
        return max_sum