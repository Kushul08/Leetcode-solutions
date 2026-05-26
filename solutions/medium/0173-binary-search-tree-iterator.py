# ─────────────────────────────────────────────────
#  Problem : 0173. Binary Search Tree Iterator
#  Difficulty : Medium
#  Runtime  : 46 ms
#  Memory   : 21.2 MB
#  Solved   : 2026-05-26
# ─────────────────────────────────────────────────

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: Optional[TreeNode]
        """
        self.stack=[root]
        node=root
        while node.left:
            node=node.left
            self.stack.append(node)
        
    def next(self):

        """
        :rtype: int
        """
        node=self.stack.pop()
        val=node.val
        print()
        if node.right:
            node=node.right
            self.stack.append(node)
            while node.left:
                node=node.left
                self.stack.append(node)
        return val

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.stack)!=0

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()