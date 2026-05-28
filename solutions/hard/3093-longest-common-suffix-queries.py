# ─────────────────────────────────────────────────
#  Problem : 3093. Longest Common Suffix Queries
#  Difficulty : Hard
#  Runtime  : 5185 ms
#  Memory   : 341 MB
#  Solved   : 2026-05-28
# ─────────────────────────────────────────────────

class Trie:
    def __init__(self):
        self.children={}
        self.best=(float('inf'),float('inf'))
    
class Solution(object):
    def stringIndices(self, wordsContainer, wordsQuery):
        """
        :type wordsContainer: List[str]
        :type wordsQuery: List[str]
        :rtype: List[int]
        """
        root=Trie()
        for i,word in enumerate(wordsContainer):
            node=root
            best=(len(word),i)

            if best<node.best:
                node.best=best
            for ch in reversed(word):
                if ch not in node.children:
                    node.children[ch]=Trie()
                node=node.children[ch]

                if best<node.best:
                    node.best=best
        
        ans=[]

        for i,word in enumerate(wordsQuery):
            node=root
            for ch in reversed(word):

                if ch not in node.children:
                    break
                node=node.children[ch]
            ans.append(node.best[1])
        return ans