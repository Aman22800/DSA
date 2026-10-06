class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack=[]
        count=0

        for i in s:
            if i=="(":
                stack.append("(")
            elif i==")":
                if not stack:
                    stack.append(i)
                else:
                    if stack[-1]=="(":
                        stack.pop()
                    else:
                        stack.append(i)

                    
            #print(stack)
        return len(stack)

        