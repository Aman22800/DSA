class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict={}
        for i in range(len(nums)):
            e=target-nums[i]
            if e in dict:
                return [dict[e],i]
            dict[nums[i]]=i



        