class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dict={}
        for i in range(len(nums)):
            if nums[i] in dict:
                if abs(dict[nums[i]]-i)<=k:
                    return True
            dict[nums[i]]=i
        return False
            

        