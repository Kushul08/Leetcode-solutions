# ─────────────────────────────────────────────────
#  Problem : 0126. Word Ladder II
#  Difficulty : Hard
#  Runtime  : 0 ms
#  Memory   : 12.5 MB
#  Solved   : 2026-06-07
# ─────────────────────────────────────────────────

from collections import deque
class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        words=set(wordList)
        queue=deque([[beginWord]])
        if endWord not in words:
            return []
        if beginWord in words:
            words.remove(beginWord)
        ans=[]
        n=0
        while queue:
            if n==0: 
                n=len(queue)
                removals=set()
            arr=queue.popleft()
            if arr[-1]==endWord:
                ans.append(arr)
                continue
            word=list(arr[-1])
            
            for i in range(len(word)):
                org=word[i]
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    word[i]=c
                    new_word=''.join(word)
                    if new_word in words:
                        temp=arr[:]
                        temp.append(new_word)
                        queue.append(temp)
                        removals.add(new_word)
                word[i]=org
            n-=1
            if n==0:
                for w in removals:
                    words.remove(w)
        return ans