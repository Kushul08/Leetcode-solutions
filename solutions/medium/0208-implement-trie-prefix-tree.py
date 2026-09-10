# ─────────────────────────────────────────────────
#  Problem : 0208. Implement Trie (Prefix Tree)
#  Difficulty : Medium
#  Runtime  : 32 ms
#  Memory   : 31.5 MB
#  Solved   : 2026-09-10
# ─────────────────────────────────────────────────

class Trie:

    def __init__(self):
        self.trie={}

    def insert(self, word: str) -> None:
        trie=self.trie
        for char in word:
            if char not in trie:
                trie[char]={}
            trie=trie[char]
        trie['end']=True

    def search(self, word: str) -> bool:
        trie=self.trie
        for char in word:
            if char not in trie:
                return False
            trie=trie[char]
        if 'end' in trie:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        trie=self.trie
        for char in prefix:
            if char not in trie:
                return False
            trie=trie[char]
        return True



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)