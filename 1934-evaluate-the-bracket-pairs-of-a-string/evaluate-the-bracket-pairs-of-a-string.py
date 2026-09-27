class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        stack=[]
        hash={}

        for key,val in knowledge:
            hash[key]=val

        curr=""
        for i in s:
            if i=="(":
                stack.append(curr)
                curr=""
            elif i==")":
                value = hash.get(curr, "?")
                curr = stack.pop() + value
            else:
                curr+=i
            #print(curr,stack)
        return curr
                
            
        