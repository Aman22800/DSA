class Solution:
    def maxDepth(self, s: str) -> int:
        curr_count=0
        max_count=0

        for i in s:
            if i=="(":
                curr_count+=1
                max_count=max(curr_count,max_count)
            elif i==")":
                curr_count-=1
        return max_count
        