class Solution:
    def checkString(self, s: str) -> bool:
        for i in range(len(s)):
            if s[i]=="b":
                b=i
                break
        if i==len(s)-1:
            return True
        for i in range(i,len(s)):
            if s[i]=="a":
                return False
        return True
        