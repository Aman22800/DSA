class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        result=[]

        def paren(o,c,curr):
            if o==c==0:
                result.append(curr)
                return

            if o>0:
                paren(o-1,c,curr+"(")
            if o<c:
                paren(o,c-1,curr+")")
        paren(n,n,"")
        return result