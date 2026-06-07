# ─────────────────────────────────────────────────
#  Problem : 0126. Word Ladder II
#  Difficulty : Hard
#  Runtime  : 71 ms
#  Memory   : 12.6 MB
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

        mpp={}
        mpp[beginWord]=1
        queue=deque([beginWord])
        words=set(wordList)
        if endWord not in words:
            return []
        if beginWord in words:
            words.remove(beginWord)
        sz=len(beginWord)
        while queue:
            element=queue.popleft()
            step=mpp[element]
            if element==endWord:
                break
            word=list(element)
            for i in range(sz):
                org=word[i]
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    word[i]=c
                    new_word=''.join(word)
                    if new_word in words:
                        queue.append(new_word)
                        mpp[new_word]=step+1
                        words.remove(new_word)
                word[i]=org
        ans=[]
        def dfs(string,arr):
            if string==beginWord:
                ans.append(arr[::-1])
                return
            step=mpp[string]
            word=list(string)

            for i in range(sz):
                org=word[i]
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    word[i]=c
                    new_word=''.join(word)
                    if new_word in mpp:
                        if mpp[new_word]+1==step:
                            arr.append(new_word)
                            dfs(new_word,arr)
                            arr.pop()
                word[i]=org
        dfs(endWord,[endWord])
        return ans