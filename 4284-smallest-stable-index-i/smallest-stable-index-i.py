class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        currmax=float('-inf')

        for i in range(len(nums)):
            currmax=max(currmax,nums[i])
            currmin=min(nums[i:])

            score=currmax-currmin
            if score<=k:
                return i
        return -1




            
            

        