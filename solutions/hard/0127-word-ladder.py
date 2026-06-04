# ─────────────────────────────────────────────────
#  Problem : 0127. Word Ladder
#  Difficulty : Hard
#  Runtime  : 548 ms
#  Memory   : 13 MB
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
        print(words)
        if beginWord in words:
            words.remove(beginWord)
        def check(s1,s2):
            count=0
            for a,b in zip(s1,s2):
                if count>1: return False
                if a!=b:
                    count+=1
            if count==1:
                return True
            return False
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