# ─────────────────────────────────────────────────
#  Problem : 2095. Delete the Middle Node of a Linked List
#  Difficulty : Medium
#  Runtime  : 71 ms
#  Memory   : 91.6 MB
#  Solved   : 2026-06-15
# ─────────────────────────────────────────────────

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        slow=head
        fast=head
        prev=None
        while fast and fast.next:
            prev=slow
            slow=slow.next
            fast=fast.next.next
        if prev==None:
            return None
        prev.next=slow.next
        return head