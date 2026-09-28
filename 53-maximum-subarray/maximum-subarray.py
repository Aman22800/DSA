class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        maxsum=nums[0]
        currsum=nums[0]

        for i in range(1,len(nums)):
            currsum=max(nums[i],currsum+nums[i])
            maxsum=max(currsum,maxsum)
        return maxsum
        