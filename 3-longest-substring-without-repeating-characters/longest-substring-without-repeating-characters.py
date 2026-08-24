class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        dict={}
        longest=float('-inf')
        if s=="":
            return 0
        for r in range(len(s)):
            if s[r] not in dict:
                dict[s[r]]=1
                longest=max(longest,r-l+1)
            else:
                while s[r] in dict:
                    del dict[s[l]]
                    l+=1
                dict[s[r]] = 1

        return longest


        