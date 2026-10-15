class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        result=0
        for i in nums:
            result=i^result
            
        return result

        