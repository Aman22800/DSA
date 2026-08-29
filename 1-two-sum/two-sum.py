class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict={}
        for i in range(len(nums)):
            if nums[i] not in dict:
                dict[nums[i]]=i
            
        print(dict)
        for j in range(len(nums)):
            e=target-nums[j]
            if e in dict and dict[e] != j:
                return [j,dict[e]]



        