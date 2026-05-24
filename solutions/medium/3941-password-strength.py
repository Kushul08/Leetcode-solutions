# ─────────────────────────────────────────────────
#  Problem : 3941. Password Strength
#  Difficulty : Medium
#  Runtime  : 15 ms
#  Memory   : 12.8 MB
#  Solved   : 2026-05-24
# ─────────────────────────────────────────────────

class Solution(object):
    def passwordStrength(self, password):
        """
        :type password: str
        :rtype: int
        """
        new_pass=set(password)
        a=ord('a')
        z=ord('z')
        A=ord('A')
        Z=ord('Z')
        strength=0
        for ch in new_pass:
            val=ord(ch)
            if a<=val and val<=z:
                strength+=1
            elif A<=val and val<=Z:
                strength+=2
            elif ch.isdigit():
                strength+=3
            else:
                strength+=5
        return strength