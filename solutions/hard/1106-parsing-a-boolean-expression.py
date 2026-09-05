# ─────────────────────────────────────────────────
#  Problem : 1106. Parsing A Boolean Expression
#  Difficulty : Hard
#  Runtime  : 37 ms
#  Memory   : 12.5 MB
#  Solved   : 2026-09-05
# ─────────────────────────────────────────────────

class Solution(object):
    def parseBoolExpr(self, expression):
        """
        :type expression: str
        :rtype: bool
        """
        stack=[]
        for ch in expression:
            if ch in '&|!':
                stack.append(ch)
            elif ch in 'tf':
                stack.append(True if ch=='t' else False)
            elif ch==')':
                seen_t=False
                seen_f=False
                while stack and (stack[-1]==True or stack[-1]==False):
                    val=stack.pop()
                    if val==False:
                        seen_f=True
                    else:
                        seen_t=True
                
                opr=stack.pop()
                if opr=='&':
                    stack.append(seen_f==False)
                elif opr=='|':
                    stack.append(seen_t==True)
                else:
                    stack.append(False if seen_t==True else True)
        return stack[0]