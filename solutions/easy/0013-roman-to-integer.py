# ─────────────────────────────────────────────────
#  Problem : 0013. Roman to Integer
#  Difficulty : Easy
#  Runtime  : 14 ms
#  Memory   : 12.5 MB
#  Solved   : 2026-08-11
# ─────────────────────────────────────────────────

class Solution(object):
    def romanToInt(self, s):
        result,i=0,0
        roman_numbers={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        while i<(len(s)):
            if i==len(s)-1:
                result+=roman_numbers[s[i]]
                break
            if roman_numbers[s[i]]>=roman_numbers[s[i+1]]:
                result+=(roman_numbers[s[i]])
                i+=1
            elif roman_numbers[s[i]]<roman_numbers[s[i+1]]:
                result+=(roman_numbers[s[i+1]]-roman_numbers[s[i]])
                i+=2
        return result


        

      

        