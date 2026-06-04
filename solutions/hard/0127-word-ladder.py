# ─────────────────────────────────────────────────
#  Problem : 0127. Word Ladder
#  Difficulty : Hard
#  Runtime  : 491 ms
#  Memory   : 12.9 MB
#  Solved   : 2026-06-04
# ─────────────────────────────────────────────────

from collections import deque
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if endWord not in wordList:
            return 0
        queue=deque()
        queue.append((beginWord,1))
        words=set(wordList)
        if beginWord in words:
            words.remove(beginWord)
        while queue:
            node,step=queue.popleft()
            if node==endWord:
                return step
            word=list(node)
            for i in range(len(word)):
                original=word[i]
                for j in range(97,123):
                    word[i]=chr(j)
                    new_word=''.join(word)
                    if new_word in words:
                        queue.append((new_word,step+1))
                        words.remove(new_word)
                word[i]=original
        return 0