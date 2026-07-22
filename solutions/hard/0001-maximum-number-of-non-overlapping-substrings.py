# ─────────────────────────────────────────────────
#  Problem : 0001. Maximum Number of Non-Overlapping Substrings
#  Difficulty : Hard
#  Runtime  : 299 ms
#  Memory   : 13.3 MB
#  Solved   : 2026-07-22
# ─────────────────────────────────────────────────

class Solution(object):
    def maxNumOfSubstrings(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        hashmap={}
        for i,ch in enumerate(s):
            if ch in hashmap:
                hashmap[ch][1]=i
            else:
                hashmap[ch]=[i,i]
        def getInterval(ch):
            L = hashmap[ch][0]
            R = hashmap[ch][1]

            i = L

            while i <= R:
                c = s[i]

                if hashmap[c][0]< L:
                    return None      # invalid interval

                R = max(R, hashmap[c][1])

                i += 1

            return (L, R)
        intervals={}
        for ch in hashmap:
            interval=getInterval(ch)
            if interval is not None:
                intervals[ch]=interval
        # Now the problem simplifies to max no of intervals which are non overlapping
        # print(intervals)
        intervals=sorted(intervals.values(), key=lambda item:item[1])
        # print(intervals)
        max_intervals=[]
        current=-1
        for a,b in intervals:
            if a>current:
                max_intervals.append([a,b])
                current=b
        # print(max_intervals)
        substrings=[]
        for a,b in max_intervals:
            substrings.append(s[a:b+1])
        return substrings