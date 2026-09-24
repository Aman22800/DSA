class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        idx=0
        for i in nums:
            num=sum(int(x) for x in str(i))
            if num==idx:
                return idx
            idx+=1
        return -1
        