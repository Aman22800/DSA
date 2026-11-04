class Solution:
    def minMoves(self, nums: List[int]) -> int:
        maxx=max(nums)
      
        res=0
        for i in nums:
            res+=abs(maxx-i)
        return res

        