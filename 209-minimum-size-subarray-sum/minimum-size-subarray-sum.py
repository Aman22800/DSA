class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l=0
        r=0
        minwindow=float('inf')
        curr=0
        print(curr)
        while r<len(nums) or curr >= target:
            if curr>=target :
                minwindow=min(minwindow,r-l)
                curr-=nums[l]
                l+=1
            elif curr<target:
                curr+=nums[r]
                r+=1
            print(curr)
        return minwindow if minwindow!=float('inf') else 0
            

        


        