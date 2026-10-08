class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        balance=0
        ans=""
        for i in s:
            if i=="(":
                balance+=1
                if balance>1:
                    ans+=i
            elif i==")":
                balance-=1
                if balance>0:
                    ans+=i
            
            #print(ans)
        return ans


        