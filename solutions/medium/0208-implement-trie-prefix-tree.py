# ─────────────────────────────────────────────────
#  Problem : 0208. Implement Trie (Prefix Tree)
#  Difficulty : Medium
#  Runtime  : 186 ms
#  Memory   : 39.4 MB
#  Solved   : 2026-09-10
# ─────────────────────────────────────────────────

class Node:
    def __init__(self,val=None,next=None):
        self.links=[0]*26
        self.flag=False
class Trie(object):

    def __init__(self):
        self.root=Node()    
    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        node=self.root
        for ch in word:
            if node.links[ord(ch)-97]==0:
                newnode=Node()
                node.links[ord(ch)-97]=newnode
                node=newnode
            else:
                node=node.links[ord(ch)-97]
        node.flag=True
    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        node=self.root
        for ch in word:
            if node.links[ord(ch)-97]==0:
                return False
            node=node.links[ord(ch)-97]
        return node.flag

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        node=self.root
        for ch in prefix:
            if node.links[ord(ch)-97]==0:
                return False
            node=node.links[ord(ch)-97]
        return True
# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)