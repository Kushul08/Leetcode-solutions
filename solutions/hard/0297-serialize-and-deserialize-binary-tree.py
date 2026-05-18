# ─────────────────────────────────────────────────
#  Problem : 0297. Serialize and Deserialize Binary Tree
#  Difficulty : Hard
#  Runtime  : 88 ms
#  Memory   : 22.7 MB
#  Solved   : 2026-05-18
# ─────────────────────────────────────────────────

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ''
        queue=deque([root])
        string=[]
        while queue:
            node=queue.popleft()
            if node is None:
                string.append('None,')
            else:
                string.append(str(node.val))
                string.append(',')
                queue.append(node.left)
                queue.append(node.right)
        return ''.join(string)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        ls=data.split(',')
        root=TreeNode(int(ls[0]))
        queue=deque([])
        queue.append(root)
        i=1
        while queue and i<len(ls):
            node=queue.popleft()
            if ls[i]!='None':
                left=TreeNode(int(ls[i]))
                node.left=left
                queue.append(left)
            i+=1
            if ls[i]!='None':
                right=TreeNode(int(ls[i]))
                node.right=right
                queue.append(right)
            i+=1
        return root



# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))